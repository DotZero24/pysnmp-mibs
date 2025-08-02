_I='macAddr'
_H='TPLINK-MAC-VLAN-MIB'
_G='ifIndex'
_F='IF-MIB'
_E='read-only'
_D='Integer32'
_C='read-create'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
TPRowStatus,=mibBuilder.importSymbols('TPLINK-TC-MIB','TPRowStatus')
tplinkMacVlanMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,15))
if mibBuilder.loadTexts:tplinkMacVlanMIB.setRevisions(('2009-08-03 00:00',))
_TplinkMacVlanMIBObjects_ObjectIdentity=ObjectIdentity
tplinkMacVlanMIBObjects=_TplinkMacVlanMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,15,1))
_MacVlanConfig_ObjectIdentity=ObjectIdentity
macVlanConfig=_MacVlanConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,15,1,1))
_MacVlanConfigTable_Object=MibTable
macVlanConfigTable=_MacVlanConfigTable_Object((1,3,6,1,4,1,11863,6,15,1,1,1))
if mibBuilder.loadTexts:macVlanConfigTable.setStatus(_A)
_MacVlanEntry_Object=MibTableRow
macVlanEntry=_MacVlanEntry_Object((1,3,6,1,4,1,11863,6,15,1,1,1,1))
macVlanEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:macVlanEntry.setStatus(_A)
_MacAddr_Type=OctetString
_MacAddr_Object=MibTableColumn
macAddr=_MacAddr_Object((1,3,6,1,4,1,11863,6,15,1,1,1,1,1),_MacAddr_Type())
macAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:macAddr.setStatus(_A)
class _MacDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_MacDescription_Type.__name__=_B
_MacDescription_Object=MibTableColumn
macDescription=_MacDescription_Object((1,3,6,1,4,1,11863,6,15,1,1,1,1,2),_MacDescription_Type())
macDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:macDescription.setStatus(_A)
class _MacVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_MacVlanId_Type.__name__=_D
_MacVlanId_Object=MibTableColumn
macVlanId=_MacVlanId_Object((1,3,6,1,4,1,11863,6,15,1,1,1,1,3),_MacVlanId_Type())
macVlanId.setMaxAccess(_C)
if mibBuilder.loadTexts:macVlanId.setStatus(_A)
_MacVlanStatus_Type=TPRowStatus
_MacVlanStatus_Object=MibTableColumn
macVlanStatus=_MacVlanStatus_Object((1,3,6,1,4,1,11863,6,15,1,1,1,1,4),_MacVlanStatus_Type())
macVlanStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:macVlanStatus.setStatus(_A)
_MacVlanPort_ObjectIdentity=ObjectIdentity
macVlanPort=_MacVlanPort_ObjectIdentity((1,3,6,1,4,1,11863,6,15,1,2))
_MacVlanPortTable_Object=MibTable
macVlanPortTable=_MacVlanPortTable_Object((1,3,6,1,4,1,11863,6,15,1,2,1))
if mibBuilder.loadTexts:macVlanPortTable.setStatus(_A)
_MacVlanPortEntry_Object=MibTableRow
macVlanPortEntry=_MacVlanPortEntry_Object((1,3,6,1,4,1,11863,6,15,1,2,1,1))
macVlanPortEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:macVlanPortEntry.setStatus(_A)
class _MacVlanPortNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_MacVlanPortNumber_Type.__name__=_B
_MacVlanPortNumber_Object=MibTableColumn
macVlanPortNumber=_MacVlanPortNumber_Object((1,3,6,1,4,1,11863,6,15,1,2,1,1,1),_MacVlanPortNumber_Type())
macVlanPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:macVlanPortNumber.setStatus(_A)
class _MacVlanPortEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('disable',0),('enable',1)))
_MacVlanPortEnable_Type.__name__=_D
_MacVlanPortEnable_Object=MibTableColumn
macVlanPortEnable=_MacVlanPortEnable_Object((1,3,6,1,4,1,11863,6,15,1,2,1,1,2),_MacVlanPortEnable_Type())
macVlanPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:macVlanPortEnable.setStatus(_A)
class _MacVlanPortLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,10))
_MacVlanPortLag_Type.__name__=_B
_MacVlanPortLag_Object=MibTableColumn
macVlanPortLag=_MacVlanPortLag_Object((1,3,6,1,4,1,11863,6,15,1,2,1,1,3),_MacVlanPortLag_Type())
macVlanPortLag.setMaxAccess(_E)
if mibBuilder.loadTexts:macVlanPortLag.setStatus(_A)
_TplinkMacVlanNotifications_ObjectIdentity=ObjectIdentity
tplinkMacVlanNotifications=_TplinkMacVlanNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,15,2))
mibBuilder.exportSymbols(_H,**{'tplinkMacVlanMIB':tplinkMacVlanMIB,'tplinkMacVlanMIBObjects':tplinkMacVlanMIBObjects,'macVlanConfig':macVlanConfig,'macVlanConfigTable':macVlanConfigTable,'macVlanEntry':macVlanEntry,_I:macAddr,'macDescription':macDescription,'macVlanId':macVlanId,'macVlanStatus':macVlanStatus,'macVlanPort':macVlanPort,'macVlanPortTable':macVlanPortTable,'macVlanPortEntry':macVlanPortEntry,'macVlanPortNumber':macVlanPortNumber,'macVlanPortEnable':macVlanPortEnable,'macVlanPortLag':macVlanPortLag,'tplinkMacVlanNotifications':tplinkMacVlanNotifications})