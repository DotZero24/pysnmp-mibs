_C='current'
_B='read-only'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lhnModules,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-GLOBAL-REG','lhnModules')
lhnNusCommonStatus,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-NUS-COMMON-MIB','lhnNusCommonStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
lhnNusCommonStatusModule=ModuleIdentity((1,3,6,1,4,1,9804,1,1,99))
class _Status_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('online',1),('offline',2)))
_Status_Type.__name__=_A
_Status_Object=MibScalar
status=_Status_Object((1,3,6,1,4,1,9804,3,1,1,2,99,1),_Status_Type())
status.setMaxAccess(_B)
if mibBuilder.loadTexts:status.setStatus(_C)
_StatusMessage_Type=OctetString
_StatusMessage_Object=MibScalar
statusMessage=_StatusMessage_Object((1,3,6,1,4,1,9804,3,1,1,2,99,2),_StatusMessage_Type())
statusMessage.setMaxAccess(_B)
if mibBuilder.loadTexts:statusMessage.setStatus(_C)
mibBuilder.exportSymbols('LEFTHAND-NETWORKS-NUS-COMMON-STATUS-MIB',**{'lhnNusCommonStatusModule':lhnNusCommonStatusModule,'status':status,'statusMessage':statusMessage})