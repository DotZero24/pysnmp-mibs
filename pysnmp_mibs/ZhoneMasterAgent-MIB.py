_D='read-write'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zhoneMasterAgent,zhoneModules=mibBuilder.importSymbols('Zhone','zhoneMasterAgent','zhoneModules')
zhoneMasterAgentMIB=ModuleIdentity((1,3,6,1,4,1,5504,6,10))
if mibBuilder.loadTexts:zhoneMasterAgentMIB.setRevisions(('2000-09-12 11:16',))
class _MaRequestPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MaRequestPort_Type.__name__=_C
_MaRequestPort_Object=MibScalar
maRequestPort=_MaRequestPort_Object((1,3,6,1,4,1,5504,3,7,1),_MaRequestPort_Type())
maRequestPort.setMaxAccess(_D)
if mibBuilder.loadTexts:maRequestPort.setStatus(_A)
class _MaTrapPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MaTrapPort_Type.__name__=_C
_MaTrapPort_Object=MibScalar
maTrapPort=_MaTrapPort_Object((1,3,6,1,4,1,5504,3,7,2),_MaTrapPort_Type())
maTrapPort.setMaxAccess(_D)
if mibBuilder.loadTexts:maTrapPort.setStatus(_A)
_MaPerfSaRequests_Type=Counter32
_MaPerfSaRequests_Object=MibScalar
maPerfSaRequests=_MaPerfSaRequests_Object((1,3,6,1,4,1,5504,3,7,3),_MaPerfSaRequests_Type())
maPerfSaRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:maPerfSaRequests.setStatus(_A)
_MaPerfSaResponses_Type=Counter32
_MaPerfSaResponses_Object=MibScalar
maPerfSaResponses=_MaPerfSaResponses_Object((1,3,6,1,4,1,5504,3,7,4),_MaPerfSaResponses_Type())
maPerfSaResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:maPerfSaResponses.setStatus(_A)
_MaPerfSnmpErrors_Type=Counter32
_MaPerfSnmpErrors_Object=MibScalar
maPerfSnmpErrors=_MaPerfSnmpErrors_Object((1,3,6,1,4,1,5504,3,7,5),_MaPerfSnmpErrors_Type())
maPerfSnmpErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:maPerfSnmpErrors.setStatus(_A)
_MaPerfSaTimeouts_Type=Counter32
_MaPerfSaTimeouts_Object=MibScalar
maPerfSaTimeouts=_MaPerfSaTimeouts_Object((1,3,6,1,4,1,5504,3,7,6),_MaPerfSaTimeouts_Type())
maPerfSaTimeouts.setMaxAccess(_B)
if mibBuilder.loadTexts:maPerfSaTimeouts.setStatus(_A)
mibBuilder.exportSymbols('ZhoneMasterAgent-MIB',**{'maRequestPort':maRequestPort,'maTrapPort':maTrapPort,'maPerfSaRequests':maPerfSaRequests,'maPerfSaResponses':maPerfSaResponses,'maPerfSnmpErrors':maPerfSnmpErrors,'maPerfSaTimeouts':maPerfSaTimeouts,'zhoneMasterAgentMIB':zhoneMasterAgentMIB})