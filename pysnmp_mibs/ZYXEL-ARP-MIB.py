_N='zyArpVid'
_M='zyArpIpAddress'
_L='zyStaticArpPort'
_K='zyStaticArpVlan'
_J='zyStaticArpMacAddress'
_I='zyStaticArpIpAddrress'
_H='read-write'
_G='dot1dBasePort'
_F='BRIDGE-MIB'
_E='read-only'
_D='Integer32'
_C='not-accessible'
_B='ZYXEL-ARP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelArp=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,11))
_ZyxelArpSetup_ObjectIdentity=ObjectIdentity
zyxelArpSetup=_ZyxelArpSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,11,1))
_ZyxelArpLearningPortTable_Object=MibTable
zyxelArpLearningPortTable=_ZyxelArpLearningPortTable_Object((1,3,6,1,4,1,890,1,15,3,11,1,1))
if mibBuilder.loadTexts:zyxelArpLearningPortTable.setStatus(_A)
_ZyxelArpLearningPortEntry_Object=MibTableRow
zyxelArpLearningPortEntry=_ZyxelArpLearningPortEntry_Object((1,3,6,1,4,1,890,1,15,3,11,1,1,1))
zyxelArpLearningPortEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:zyxelArpLearningPortEntry.setStatus(_A)
class _ZyArpLearningPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('arpReply',0),('gratuitousArp',1),('arpRequest',2)))
_ZyArpLearningPortMode_Type.__name__=_D
_ZyArpLearningPortMode_Object=MibTableColumn
zyArpLearningPortMode=_ZyArpLearningPortMode_Object((1,3,6,1,4,1,890,1,15,3,11,1,1,1,1),_ZyArpLearningPortMode_Type())
zyArpLearningPortMode.setMaxAccess(_H)
if mibBuilder.loadTexts:zyArpLearningPortMode.setStatus(_A)
_ZyArpAgingTime_Type=Integer32
_ZyArpAgingTime_Object=MibScalar
zyArpAgingTime=_ZyArpAgingTime_Object((1,3,6,1,4,1,890,1,15,3,11,1,2),_ZyArpAgingTime_Type())
zyArpAgingTime.setMaxAccess(_H)
if mibBuilder.loadTexts:zyArpAgingTime.setStatus(_A)
_ZyStaticArpMaxNumberOfArps_Type=Integer32
_ZyStaticArpMaxNumberOfArps_Object=MibScalar
zyStaticArpMaxNumberOfArps=_ZyStaticArpMaxNumberOfArps_Object((1,3,6,1,4,1,890,1,15,3,11,1,3),_ZyStaticArpMaxNumberOfArps_Type())
zyStaticArpMaxNumberOfArps.setMaxAccess(_E)
if mibBuilder.loadTexts:zyStaticArpMaxNumberOfArps.setStatus(_A)
_ZyxelStaticArpTable_Object=MibTable
zyxelStaticArpTable=_ZyxelStaticArpTable_Object((1,3,6,1,4,1,890,1,15,3,11,1,4))
if mibBuilder.loadTexts:zyxelStaticArpTable.setStatus(_A)
_ZyxelStaticArpEntry_Object=MibTableRow
zyxelStaticArpEntry=_ZyxelStaticArpEntry_Object((1,3,6,1,4,1,890,1,15,3,11,1,4,1))
zyxelStaticArpEntry.setIndexNames((0,_B,_I),(0,_B,_J),(0,_B,_K),(0,_B,_L))
if mibBuilder.loadTexts:zyxelStaticArpEntry.setStatus(_A)
_ZyStaticArpIpAddrress_Type=IpAddress
_ZyStaticArpIpAddrress_Object=MibTableColumn
zyStaticArpIpAddrress=_ZyStaticArpIpAddrress_Object((1,3,6,1,4,1,890,1,15,3,11,1,4,1,1),_ZyStaticArpIpAddrress_Type())
zyStaticArpIpAddrress.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStaticArpIpAddrress.setStatus(_A)
_ZyStaticArpMacAddress_Type=MacAddress
_ZyStaticArpMacAddress_Object=MibTableColumn
zyStaticArpMacAddress=_ZyStaticArpMacAddress_Object((1,3,6,1,4,1,890,1,15,3,11,1,4,1,2),_ZyStaticArpMacAddress_Type())
zyStaticArpMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStaticArpMacAddress.setStatus(_A)
class _ZyStaticArpVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_ZyStaticArpVlan_Type.__name__=_D
_ZyStaticArpVlan_Object=MibTableColumn
zyStaticArpVlan=_ZyStaticArpVlan_Object((1,3,6,1,4,1,890,1,15,3,11,1,4,1,3),_ZyStaticArpVlan_Type())
zyStaticArpVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStaticArpVlan.setStatus(_A)
_ZyStaticArpPort_Type=Integer32
_ZyStaticArpPort_Object=MibTableColumn
zyStaticArpPort=_ZyStaticArpPort_Object((1,3,6,1,4,1,890,1,15,3,11,1,4,1,4),_ZyStaticArpPort_Type())
zyStaticArpPort.setMaxAccess(_C)
if mibBuilder.loadTexts:zyStaticArpPort.setStatus(_A)
_ZyStaticArpRowStatus_Type=RowStatus
_ZyStaticArpRowStatus_Object=MibTableColumn
zyStaticArpRowStatus=_ZyStaticArpRowStatus_Object((1,3,6,1,4,1,890,1,15,3,11,1,4,1,5),_ZyStaticArpRowStatus_Type())
zyStaticArpRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyStaticArpRowStatus.setStatus(_A)
_ZyxelArpStatus_ObjectIdentity=ObjectIdentity
zyxelArpStatus=_ZyxelArpStatus_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,11,2))
_ZyxelArpTable_Object=MibTable
zyxelArpTable=_ZyxelArpTable_Object((1,3,6,1,4,1,890,1,15,3,11,2,1))
if mibBuilder.loadTexts:zyxelArpTable.setStatus(_A)
_ZyxelArpEntry_Object=MibTableRow
zyxelArpEntry=_ZyxelArpEntry_Object((1,3,6,1,4,1,890,1,15,3,11,2,1,1))
zyxelArpEntry.setIndexNames((0,_B,_M),(0,_B,_N))
if mibBuilder.loadTexts:zyxelArpEntry.setStatus(_A)
_ZyArpIpAddress_Type=IpAddress
_ZyArpIpAddress_Object=MibTableColumn
zyArpIpAddress=_ZyArpIpAddress_Object((1,3,6,1,4,1,890,1,15,3,11,2,1,1,1),_ZyArpIpAddress_Type())
zyArpIpAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:zyArpIpAddress.setStatus(_A)
_ZyArpVid_Type=Integer32
_ZyArpVid_Object=MibTableColumn
zyArpVid=_ZyArpVid_Object((1,3,6,1,4,1,890,1,15,3,11,2,1,1,2),_ZyArpVid_Type())
zyArpVid.setMaxAccess(_C)
if mibBuilder.loadTexts:zyArpVid.setStatus(_A)
_ZyArpMacAddress_Type=MacAddress
_ZyArpMacAddress_Object=MibTableColumn
zyArpMacAddress=_ZyArpMacAddress_Object((1,3,6,1,4,1,890,1,15,3,11,2,1,1,3),_ZyArpMacAddress_Type())
zyArpMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:zyArpMacAddress.setStatus(_A)
_ZyArpPort_Type=Integer32
_ZyArpPort_Object=MibTableColumn
zyArpPort=_ZyArpPort_Object((1,3,6,1,4,1,890,1,15,3,11,2,1,1,4),_ZyArpPort_Type())
zyArpPort.setMaxAccess(_E)
if mibBuilder.loadTexts:zyArpPort.setStatus(_A)
class _ZyArpType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('static',1),('dynamic',2)))
_ZyArpType_Type.__name__=_D
_ZyArpType_Object=MibTableColumn
zyArpType=_ZyArpType_Object((1,3,6,1,4,1,890,1,15,3,11,2,1,1,5),_ZyArpType_Type())
zyArpType.setMaxAccess(_E)
if mibBuilder.loadTexts:zyArpType.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zyxelArp':zyxelArp,'zyxelArpSetup':zyxelArpSetup,'zyxelArpLearningPortTable':zyxelArpLearningPortTable,'zyxelArpLearningPortEntry':zyxelArpLearningPortEntry,'zyArpLearningPortMode':zyArpLearningPortMode,'zyArpAgingTime':zyArpAgingTime,'zyStaticArpMaxNumberOfArps':zyStaticArpMaxNumberOfArps,'zyxelStaticArpTable':zyxelStaticArpTable,'zyxelStaticArpEntry':zyxelStaticArpEntry,_I:zyStaticArpIpAddrress,_J:zyStaticArpMacAddress,_K:zyStaticArpVlan,_L:zyStaticArpPort,'zyStaticArpRowStatus':zyStaticArpRowStatus,'zyxelArpStatus':zyxelArpStatus,'zyxelArpTable':zyxelArpTable,'zyxelArpEntry':zyxelArpEntry,_M:zyArpIpAddress,_N:zyArpVid,'zyArpMacAddress':zyArpMacAddress,'zyArpPort':zyArpPort,'zyArpType':zyArpType})