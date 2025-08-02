_C='current'
_B='routing'
_A='Integer32'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_A,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
des3810_28,=mibBuilder.importSymbols('SW3810PRIMGMT-MIB','des3810-28')
swSwitchResourceMgmtMIB=ModuleIdentity((1,3,6,1,4,1,171,11,114,1,1,4))
_SwSwitchResourceMgmtMIBObjects_ObjectIdentity=ObjectIdentity
swSwitchResourceMgmtMIBObjects=_SwSwitchResourceMgmtMIBObjects_ObjectIdentity((1,3,6,1,4,1,171,11,114,1,1,4,1))
class _SwSwitchResourceMgmtSRMMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_B,1),('vpws',2)))
_SwSwitchResourceMgmtSRMMode_Type.__name__=_A
_SwSwitchResourceMgmtSRMMode_Object=MibScalar
swSwitchResourceMgmtSRMMode=_SwSwitchResourceMgmtSRMMode_Object((1,3,6,1,4,1,171,11,114,1,1,4,1,2),_SwSwitchResourceMgmtSRMMode_Type())
swSwitchResourceMgmtSRMMode.setMaxAccess('read-write')
if mibBuilder.loadTexts:swSwitchResourceMgmtSRMMode.setStatus(_C)
class _SwSwitchResourceMgmtSRMCurrentMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_B,1),('vpws',2)))
_SwSwitchResourceMgmtSRMCurrentMode_Type.__name__=_A
_SwSwitchResourceMgmtSRMCurrentMode_Object=MibScalar
swSwitchResourceMgmtSRMCurrentMode=_SwSwitchResourceMgmtSRMCurrentMode_Object((1,3,6,1,4,1,171,11,114,1,1,4,1,3),_SwSwitchResourceMgmtSRMCurrentMode_Type())
swSwitchResourceMgmtSRMCurrentMode.setMaxAccess('read-only')
if mibBuilder.loadTexts:swSwitchResourceMgmtSRMCurrentMode.setStatus(_C)
mibBuilder.exportSymbols('DES3810-28-SWITCH-RESOURCE-MGMT-MIB',**{'swSwitchResourceMgmtMIB':swSwitchResourceMgmtMIB,'swSwitchResourceMgmtMIBObjects':swSwitchResourceMgmtMIBObjects,'swSwitchResourceMgmtSRMMode':swSwitchResourceMgmtSRMMode,'swSwitchResourceMgmtSRMCurrentMode':swSwitchResourceMgmtSRMCurrentMode})