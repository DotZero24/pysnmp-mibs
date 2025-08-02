_L='zyStaticBindingMacAddress'
_K='zyStaticBindingVid'
_J='zyStaticBindingIpAddress'
_I='zyIpsgInfoMacAddress'
_H='zyIpsgInfoVid'
_G='zyIpsgInfoIpAddress'
_F='read-only'
_E='read-write'
_D='Integer32'
_C='not-accessible'
_B='ZYXEL-IPSG-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelIpsg=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,33))
_ZyxelArpFreezeSetup_ObjectIdentity=ObjectIdentity
zyxelArpFreezeSetup=_ZyxelArpFreezeSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,33,1))
_ZyArpFreeze_Type=Integer32
_ZyArpFreeze_Object=MibScalar
zyArpFreeze=_ZyArpFreeze_Object((1,3,6,1,4,1,890,1,15,3,33,1,1),_ZyArpFreeze_Type())
zyArpFreeze.setMaxAccess(_E)
if mibBuilder.loadTexts:zyArpFreeze.setStatus(_A)
_ZyArpFreezePorts_Type=PortList
_ZyArpFreezePorts_Object=MibScalar
zyArpFreezePorts=_ZyArpFreezePorts_Object((1,3,6,1,4,1,890,1,15,3,33,1,2),_ZyArpFreezePorts_Type())
zyArpFreezePorts.setMaxAccess(_E)
if mibBuilder.loadTexts:zyArpFreezePorts.setStatus(_A)
_ZyArpFreezeVlan_Type=Integer32
_ZyArpFreezeVlan_Object=MibScalar
zyArpFreezeVlan=_ZyArpFreezeVlan_Object((1,3,6,1,4,1,890,1,15,3,33,1,3),_ZyArpFreezeVlan_Type())
zyArpFreezeVlan.setMaxAccess(_E)
if mibBuilder.loadTexts:zyArpFreezeVlan.setStatus(_A)
_ZyxelIpsgStatus_ObjectIdentity=ObjectIdentity
zyxelIpsgStatus=_ZyxelIpsgStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,33,2))
_ZyxelIpsgInfoTable_Object=MibTable
zyxelIpsgInfoTable=_ZyxelIpsgInfoTable_Object((1,3,6,1,4,1,890,1,15,3,33,2,2))
if mibBuilder.loadTexts:zyxelIpsgInfoTable.setStatus(_A)
_ZyxelIpsgInfoEntry_Object=MibTableRow
zyxelIpsgInfoEntry=_ZyxelIpsgInfoEntry_Object((1,3,6,1,4,1,890,1,15,3,33,2,2,1))
zyxelIpsgInfoEntry.setIndexNames((0,_B,_G),(0,_B,_H),(0,_B,_I))
if mibBuilder.loadTexts:zyxelIpsgInfoEntry.setStatus(_A)
_ZyIpsgInfoIpAddress_Type=IpAddress
_ZyIpsgInfoIpAddress_Object=MibTableColumn
zyIpsgInfoIpAddress=_ZyIpsgInfoIpAddress_Object((1,3,6,1,4,1,890,1,15,3,33,2,2,1,1),_ZyIpsgInfoIpAddress_Type())
zyIpsgInfoIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIpsgInfoIpAddress.setStatus(_A)
class _ZyIpsgInfoVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZyIpsgInfoVid_Type.__name__=_D
_ZyIpsgInfoVid_Object=MibTableColumn
zyIpsgInfoVid=_ZyIpsgInfoVid_Object((1,3,6,1,4,1,890,1,15,3,33,2,2,1,2),_ZyIpsgInfoVid_Type())
zyIpsgInfoVid.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIpsgInfoVid.setStatus(_A)
_ZyIpsgInfoMacAddress_Type=MacAddress
_ZyIpsgInfoMacAddress_Object=MibTableColumn
zyIpsgInfoMacAddress=_ZyIpsgInfoMacAddress_Object((1,3,6,1,4,1,890,1,15,3,33,2,2,1,3),_ZyIpsgInfoMacAddress_Type())
zyIpsgInfoMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zyIpsgInfoMacAddress.setStatus(_A)
_ZyIpsgInfoLeaseTime_Type=Integer32
_ZyIpsgInfoLeaseTime_Object=MibTableColumn
zyIpsgInfoLeaseTime=_ZyIpsgInfoLeaseTime_Object((1,3,6,1,4,1,890,1,15,3,33,2,2,1,4),_ZyIpsgInfoLeaseTime_Type())
zyIpsgInfoLeaseTime.setMaxAccess(_F)
if mibBuilder.loadTexts:zyIpsgInfoLeaseTime.setStatus(_A)
class _ZyIpsgInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dhcp',2)))
_ZyIpsgInfoType_Type.__name__=_D
_ZyIpsgInfoType_Object=MibTableColumn
zyIpsgInfoType=_ZyIpsgInfoType_Object((1,3,6,1,4,1,890,1,15,3,33,2,2,1,5),_ZyIpsgInfoType_Type())
zyIpsgInfoType.setMaxAccess(_F)
if mibBuilder.loadTexts:zyIpsgInfoType.setStatus(_A)
_ZyIpsgInfoPort_Type=Integer32
_ZyIpsgInfoPort_Object=MibTableColumn
zyIpsgInfoPort=_ZyIpsgInfoPort_Object((1,3,6,1,4,1,890,1,15,3,33,2,2,1,6),_ZyIpsgInfoPort_Type())
zyIpsgInfoPort.setMaxAccess(_F)
if mibBuilder.loadTexts:zyIpsgInfoPort.setStatus(_A)
_ZyxelStaticBindingSetup_ObjectIdentity=ObjectIdentity
zyxelStaticBindingSetup=_ZyxelStaticBindingSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,33,3))
_ZyStaticBindingMaxNumberOfRules_Type=Integer32
_ZyStaticBindingMaxNumberOfRules_Object=MibScalar
zyStaticBindingMaxNumberOfRules=_ZyStaticBindingMaxNumberOfRules_Object((1,3,6,1,4,1,890,1,15,3,33,3,1),_ZyStaticBindingMaxNumberOfRules_Type())
zyStaticBindingMaxNumberOfRules.setMaxAccess(_F)
if mibBuilder.loadTexts:zyStaticBindingMaxNumberOfRules.setStatus(_A)
_ZyxelStaticBindingTable_Object=MibTable
zyxelStaticBindingTable=_ZyxelStaticBindingTable_Object((1,3,6,1,4,1,890,1,15,3,33,3,3))
if mibBuilder.loadTexts:zyxelStaticBindingTable.setStatus(_A)
_ZyxelStaticBindingEntry_Object=MibTableRow
zyxelStaticBindingEntry=_ZyxelStaticBindingEntry_Object((1,3,6,1,4,1,890,1,15,3,33,3,3,1))
zyxelStaticBindingEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:zyxelStaticBindingEntry.setStatus(_A)
_ZyStaticBindingIpAddress_Type=IpAddress
_ZyStaticBindingIpAddress_Object=MibTableColumn
zyStaticBindingIpAddress=_ZyStaticBindingIpAddress_Object((1,3,6,1,4,1,890,1,15,3,33,3,3,1,1),_ZyStaticBindingIpAddress_Type())
zyStaticBindingIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStaticBindingIpAddress.setStatus(_A)
class _ZyStaticBindingVid_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZyStaticBindingVid_Type.__name__=_D
_ZyStaticBindingVid_Object=MibTableColumn
zyStaticBindingVid=_ZyStaticBindingVid_Object((1,3,6,1,4,1,890,1,15,3,33,3,3,1,2),_ZyStaticBindingVid_Type())
zyStaticBindingVid.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStaticBindingVid.setStatus(_A)
_ZyStaticBindingMacAddress_Type=MacAddress
_ZyStaticBindingMacAddress_Object=MibTableColumn
zyStaticBindingMacAddress=_ZyStaticBindingMacAddress_Object((1,3,6,1,4,1,890,1,15,3,33,3,3,1,3),_ZyStaticBindingMacAddress_Type())
zyStaticBindingMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStaticBindingMacAddress.setStatus(_A)
_ZyStaticBindingPort_Type=Integer32
_ZyStaticBindingPort_Object=MibTableColumn
zyStaticBindingPort=_ZyStaticBindingPort_Object((1,3,6,1,4,1,890,1,15,3,33,3,3,1,4),_ZyStaticBindingPort_Type())
zyStaticBindingPort.setMaxAccess(_E)
if mibBuilder.loadTexts:zyStaticBindingPort.setStatus(_A)
_ZyStaticBindingRowStatus_Type=RowStatus
_ZyStaticBindingRowStatus_Object=MibTableColumn
zyStaticBindingRowStatus=_ZyStaticBindingRowStatus_Object((1,3,6,1,4,1,890,1,15,3,33,3,3,1,5),_ZyStaticBindingRowStatus_Type())
zyStaticBindingRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyStaticBindingRowStatus.setStatus(_A)
_ZyxelIpsgSetup_ObjectIdentity=ObjectIdentity
zyxelIpsgSetup=_ZyxelIpsgSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,33,4))
class _ZyIpsgMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('strict',1),('loose',2)))
_ZyIpsgMode_Type.__name__=_D
_ZyIpsgMode_Object=MibScalar
zyIpsgMode=_ZyIpsgMode_Object((1,3,6,1,4,1,890,1,15,3,33,4,1),_ZyIpsgMode_Type())
zyIpsgMode.setMaxAccess(_E)
if mibBuilder.loadTexts:zyIpsgMode.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zyxelIpsg':zyxelIpsg,'zyxelArpFreezeSetup':zyxelArpFreezeSetup,'zyArpFreeze':zyArpFreeze,'zyArpFreezePorts':zyArpFreezePorts,'zyArpFreezeVlan':zyArpFreezeVlan,'zyxelIpsgStatus':zyxelIpsgStatus,'zyxelIpsgInfoTable':zyxelIpsgInfoTable,'zyxelIpsgInfoEntry':zyxelIpsgInfoEntry,_G:zyIpsgInfoIpAddress,_H:zyIpsgInfoVid,_I:zyIpsgInfoMacAddress,'zyIpsgInfoLeaseTime':zyIpsgInfoLeaseTime,'zyIpsgInfoType':zyIpsgInfoType,'zyIpsgInfoPort':zyIpsgInfoPort,'zyxelStaticBindingSetup':zyxelStaticBindingSetup,'zyStaticBindingMaxNumberOfRules':zyStaticBindingMaxNumberOfRules,'zyxelStaticBindingTable':zyxelStaticBindingTable,'zyxelStaticBindingEntry':zyxelStaticBindingEntry,_J:zyStaticBindingIpAddress,_K:zyStaticBindingVid,_L:zyStaticBindingMacAddress,'zyStaticBindingPort':zyStaticBindingPort,'zyStaticBindingRowStatus':zyStaticBindingRowStatus,'zyxelIpsgSetup':zyxelIpsgSetup,'zyIpsgMode':zyIpsgMode})