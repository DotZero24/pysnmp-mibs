_B='current'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfFcoeMode=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,135))
if mibBuilder.loadTexts:hpnicfFcoeMode.setRevisions(('2013-03-08 11:00',))
_HpnicfFcoeModeMibObjects_ObjectIdentity=ObjectIdentity
hpnicfFcoeModeMibObjects=_HpnicfFcoeModeMibObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,135,1))
_HpnicfFcoeModeCfgMode_Type=Integer32
_HpnicfFcoeModeCfgMode_Object=MibScalar
hpnicfFcoeModeCfgMode=_HpnicfFcoeModeCfgMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,135,1,1),_HpnicfFcoeModeCfgMode_Type())
hpnicfFcoeModeCfgMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:hpnicfFcoeModeCfgMode.setStatus(_B)
class _HpnicfFcoeModeCfgLastResult_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('success',1),('noLicence',2),('needReset',3),('unknownFault',4)))
_HpnicfFcoeModeCfgLastResult_Type.__name__=_A
_HpnicfFcoeModeCfgLastResult_Object=MibScalar
hpnicfFcoeModeCfgLastResult=_HpnicfFcoeModeCfgLastResult_Object((1,3,6,1,4,1,11,2,14,11,15,2,135,1,2),_HpnicfFcoeModeCfgLastResult_Type())
hpnicfFcoeModeCfgLastResult.setMaxAccess('read-only')
if mibBuilder.loadTexts:hpnicfFcoeModeCfgLastResult.setStatus(_B)
mibBuilder.exportSymbols('HPN-ICF-FCOE-MODE-MIB',**{'hpnicfFcoeMode':hpnicfFcoeMode,'hpnicfFcoeModeMibObjects':hpnicfFcoeModeMibObjects,'hpnicfFcoeModeCfgMode':hpnicfFcoeModeCfgMode,'hpnicfFcoeModeCfgLastResult':hpnicfFcoeModeCfgLastResult})