_N='rcDhcp6SnoopingBindIp'
_M='rcDhcp6SnoopingPortIndex'
_L='rcDhcpSnoopingBindIp'
_K='untrusted'
_J='trusted'
_I='rcDhcpSnoopingPortIndex'
_H='OctetString'
_G='not-accessible'
_F='EnableVar'
_E='DHCP-SNOOPING-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddressIPv4,InetAddressIPv6=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressIPv4','InetAddressIPv6')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention')
EnableVar,=mibBuilder.importSymbols('SWITCH-TC',_F)
rcDhcpSnooping=ModuleIdentity((1,3,6,1,4,1,8886,6,1,23))
if mibBuilder.loadTexts:rcDhcpSnooping.setRevisions(('2010-12-10 00:00',))
_RcDhcpSnoopingMibObjects_ObjectIdentity=ObjectIdentity
rcDhcpSnoopingMibObjects=_RcDhcpSnoopingMibObjects_ObjectIdentity((1,3,6,1,4,1,8886,6,1,23,1))
_RcDhcpSnoopingGroup_ObjectIdentity=ObjectIdentity
rcDhcpSnoopingGroup=_RcDhcpSnoopingGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,23,1,1))
class _RcDhcpSnoopingEnable_Type(EnableVar):defaultValue=2
_RcDhcpSnoopingEnable_Type.__name__=_F
_RcDhcpSnoopingEnable_Object=MibScalar
rcDhcpSnoopingEnable=_RcDhcpSnoopingEnable_Object((1,3,6,1,4,1,8886,6,1,23,1,1,1),_RcDhcpSnoopingEnable_Type())
rcDhcpSnoopingEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpSnoopingEnable.setStatus(_A)
_RcDhcpSnoopingPortTable_Object=MibTable
rcDhcpSnoopingPortTable=_RcDhcpSnoopingPortTable_Object((1,3,6,1,4,1,8886,6,1,23,1,1,2))
if mibBuilder.loadTexts:rcDhcpSnoopingPortTable.setStatus(_A)
_RcDhcpSnoopingPortEntry_Object=MibTableRow
rcDhcpSnoopingPortEntry=_RcDhcpSnoopingPortEntry_Object((1,3,6,1,4,1,8886,6,1,23,1,1,2,1))
rcDhcpSnoopingPortEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:rcDhcpSnoopingPortEntry.setStatus(_A)
_RcDhcpSnoopingPortIndex_Type=Integer32
_RcDhcpSnoopingPortIndex_Object=MibTableColumn
rcDhcpSnoopingPortIndex=_RcDhcpSnoopingPortIndex_Object((1,3,6,1,4,1,8886,6,1,23,1,1,2,1,1),_RcDhcpSnoopingPortIndex_Type())
rcDhcpSnoopingPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rcDhcpSnoopingPortIndex.setStatus(_A)
_RcDhcpSnoopingPortEnable_Type=EnableVar
_RcDhcpSnoopingPortEnable_Object=MibTableColumn
rcDhcpSnoopingPortEnable=_RcDhcpSnoopingPortEnable_Object((1,3,6,1,4,1,8886,6,1,23,1,1,2,1,2),_RcDhcpSnoopingPortEnable_Type())
rcDhcpSnoopingPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpSnoopingPortEnable.setStatus(_A)
class _RcDhcpSnoopingPortTrust_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_RcDhcpSnoopingPortTrust_Type.__name__=_D
_RcDhcpSnoopingPortTrust_Object=MibTableColumn
rcDhcpSnoopingPortTrust=_RcDhcpSnoopingPortTrust_Object((1,3,6,1,4,1,8886,6,1,23,1,1,2,1,3),_RcDhcpSnoopingPortTrust_Type())
rcDhcpSnoopingPortTrust.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpSnoopingPortTrust.setStatus(_A)
class _RcDhcpSnoopingBindCurrentRows_Type(Integer32):defaultValue=0
_RcDhcpSnoopingBindCurrentRows_Type.__name__=_D
_RcDhcpSnoopingBindCurrentRows_Object=MibScalar
rcDhcpSnoopingBindCurrentRows=_RcDhcpSnoopingBindCurrentRows_Object((1,3,6,1,4,1,8886,6,1,23,1,1,3),_RcDhcpSnoopingBindCurrentRows_Type())
rcDhcpSnoopingBindCurrentRows.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpSnoopingBindCurrentRows.setStatus(_A)
class _RcDhcpSnoopingBindHistoryMaxRows_Type(Integer32):defaultValue=0
_RcDhcpSnoopingBindHistoryMaxRows_Type.__name__=_D
_RcDhcpSnoopingBindHistoryMaxRows_Object=MibScalar
rcDhcpSnoopingBindHistoryMaxRows=_RcDhcpSnoopingBindHistoryMaxRows_Object((1,3,6,1,4,1,8886,6,1,23,1,1,4),_RcDhcpSnoopingBindHistoryMaxRows_Type())
rcDhcpSnoopingBindHistoryMaxRows.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpSnoopingBindHistoryMaxRows.setStatus(_A)
_RcDhcpSnoopingBindTable_Object=MibTable
rcDhcpSnoopingBindTable=_RcDhcpSnoopingBindTable_Object((1,3,6,1,4,1,8886,6,1,23,1,1,5))
if mibBuilder.loadTexts:rcDhcpSnoopingBindTable.setStatus(_A)
_RcDhcpSnoopingBindEntry_Object=MibTableRow
rcDhcpSnoopingBindEntry=_RcDhcpSnoopingBindEntry_Object((1,3,6,1,4,1,8886,6,1,23,1,1,5,1))
rcDhcpSnoopingBindEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:rcDhcpSnoopingBindEntry.setStatus(_A)
_RcDhcpSnoopingBindIp_Type=InetAddressIPv4
_RcDhcpSnoopingBindIp_Object=MibTableColumn
rcDhcpSnoopingBindIp=_RcDhcpSnoopingBindIp_Object((1,3,6,1,4,1,8886,6,1,23,1,1,5,1,1),_RcDhcpSnoopingBindIp_Type())
rcDhcpSnoopingBindIp.setMaxAccess(_G)
if mibBuilder.loadTexts:rcDhcpSnoopingBindIp.setStatus(_A)
_RcDhcpSnoopingBindMac_Type=MacAddress
_RcDhcpSnoopingBindMac_Object=MibTableColumn
rcDhcpSnoopingBindMac=_RcDhcpSnoopingBindMac_Object((1,3,6,1,4,1,8886,6,1,23,1,1,5,1,2),_RcDhcpSnoopingBindMac_Type())
rcDhcpSnoopingBindMac.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpSnoopingBindMac.setStatus(_A)
_RcDhcpSnoopingBindLease_Type=Unsigned32
_RcDhcpSnoopingBindLease_Object=MibTableColumn
rcDhcpSnoopingBindLease=_RcDhcpSnoopingBindLease_Object((1,3,6,1,4,1,8886,6,1,23,1,1,5,1,3),_RcDhcpSnoopingBindLease_Type())
rcDhcpSnoopingBindLease.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpSnoopingBindLease.setStatus(_A)
class _RcDhcpSnoopingBindVlan_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_RcDhcpSnoopingBindVlan_Type.__name__=_D
_RcDhcpSnoopingBindVlan_Object=MibTableColumn
rcDhcpSnoopingBindVlan=_RcDhcpSnoopingBindVlan_Object((1,3,6,1,4,1,8886,6,1,23,1,1,5,1,4),_RcDhcpSnoopingBindVlan_Type())
rcDhcpSnoopingBindVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpSnoopingBindVlan.setStatus(_A)
_RcDhcpSnoopingBindPort_Type=Integer32
_RcDhcpSnoopingBindPort_Object=MibTableColumn
rcDhcpSnoopingBindPort=_RcDhcpSnoopingBindPort_Object((1,3,6,1,4,1,8886,6,1,23,1,1,5,1,5),_RcDhcpSnoopingBindPort_Type())
rcDhcpSnoopingBindPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcpSnoopingBindPort.setStatus(_A)
_RcDhcp6SnoopingGroup_ObjectIdentity=ObjectIdentity
rcDhcp6SnoopingGroup=_RcDhcp6SnoopingGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,23,1,2))
class _RcDhcp6SnoopingEnable_Type(EnableVar):defaultValue=2
_RcDhcp6SnoopingEnable_Type.__name__=_F
_RcDhcp6SnoopingEnable_Object=MibScalar
rcDhcp6SnoopingEnable=_RcDhcp6SnoopingEnable_Object((1,3,6,1,4,1,8886,6,1,23,1,2,1),_RcDhcp6SnoopingEnable_Type())
rcDhcp6SnoopingEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcp6SnoopingEnable.setStatus(_A)
_RcDhcp6SnoopingPortTable_Object=MibTable
rcDhcp6SnoopingPortTable=_RcDhcp6SnoopingPortTable_Object((1,3,6,1,4,1,8886,6,1,23,1,2,2))
if mibBuilder.loadTexts:rcDhcp6SnoopingPortTable.setStatus(_A)
_RcDhcp6SnoopingPortEntry_Object=MibTableRow
rcDhcp6SnoopingPortEntry=_RcDhcp6SnoopingPortEntry_Object((1,3,6,1,4,1,8886,6,1,23,1,2,2,1))
rcDhcp6SnoopingPortEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:rcDhcp6SnoopingPortEntry.setStatus(_A)
_RcDhcp6SnoopingPortIndex_Type=Integer32
_RcDhcp6SnoopingPortIndex_Object=MibTableColumn
rcDhcp6SnoopingPortIndex=_RcDhcp6SnoopingPortIndex_Object((1,3,6,1,4,1,8886,6,1,23,1,2,2,1,1),_RcDhcp6SnoopingPortIndex_Type())
rcDhcp6SnoopingPortIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:rcDhcp6SnoopingPortIndex.setStatus(_A)
_RcDhcp6SnoopingPortEnable_Type=EnableVar
_RcDhcp6SnoopingPortEnable_Object=MibTableColumn
rcDhcp6SnoopingPortEnable=_RcDhcp6SnoopingPortEnable_Object((1,3,6,1,4,1,8886,6,1,23,1,2,2,1,2),_RcDhcp6SnoopingPortEnable_Type())
rcDhcp6SnoopingPortEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcp6SnoopingPortEnable.setStatus(_A)
class _RcDhcp6SnoopingPortTrust_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_RcDhcp6SnoopingPortTrust_Type.__name__=_D
_RcDhcp6SnoopingPortTrust_Object=MibTableColumn
rcDhcp6SnoopingPortTrust=_RcDhcp6SnoopingPortTrust_Object((1,3,6,1,4,1,8886,6,1,23,1,2,2,1,3),_RcDhcp6SnoopingPortTrust_Type())
rcDhcp6SnoopingPortTrust.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcp6SnoopingPortTrust.setStatus(_A)
class _RcDhcp6SnoopingBindCurrentRows_Type(Integer32):defaultValue=0
_RcDhcp6SnoopingBindCurrentRows_Type.__name__=_D
_RcDhcp6SnoopingBindCurrentRows_Object=MibScalar
rcDhcp6SnoopingBindCurrentRows=_RcDhcp6SnoopingBindCurrentRows_Object((1,3,6,1,4,1,8886,6,1,23,1,2,3),_RcDhcp6SnoopingBindCurrentRows_Type())
rcDhcp6SnoopingBindCurrentRows.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcp6SnoopingBindCurrentRows.setStatus(_A)
class _RcDhcp6SnoopingBindHistoryMaxRows_Type(Integer32):defaultValue=0
_RcDhcp6SnoopingBindHistoryMaxRows_Type.__name__=_D
_RcDhcp6SnoopingBindHistoryMaxRows_Object=MibScalar
rcDhcp6SnoopingBindHistoryMaxRows=_RcDhcp6SnoopingBindHistoryMaxRows_Object((1,3,6,1,4,1,8886,6,1,23,1,2,4),_RcDhcp6SnoopingBindHistoryMaxRows_Type())
rcDhcp6SnoopingBindHistoryMaxRows.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcp6SnoopingBindHistoryMaxRows.setStatus(_A)
_RcDhcp6SnoopingBindTable_Object=MibTable
rcDhcp6SnoopingBindTable=_RcDhcp6SnoopingBindTable_Object((1,3,6,1,4,1,8886,6,1,23,1,2,5))
if mibBuilder.loadTexts:rcDhcp6SnoopingBindTable.setStatus(_A)
_RcDhcp6SnoopingBindEntry_Object=MibTableRow
rcDhcp6SnoopingBindEntry=_RcDhcp6SnoopingBindEntry_Object((1,3,6,1,4,1,8886,6,1,23,1,2,5,1))
rcDhcp6SnoopingBindEntry.setIndexNames((0,_E,_N))
if mibBuilder.loadTexts:rcDhcp6SnoopingBindEntry.setStatus(_A)
_RcDhcp6SnoopingBindIp_Type=InetAddressIPv6
_RcDhcp6SnoopingBindIp_Object=MibTableColumn
rcDhcp6SnoopingBindIp=_RcDhcp6SnoopingBindIp_Object((1,3,6,1,4,1,8886,6,1,23,1,2,5,1,1),_RcDhcp6SnoopingBindIp_Type())
rcDhcp6SnoopingBindIp.setMaxAccess(_G)
if mibBuilder.loadTexts:rcDhcp6SnoopingBindIp.setStatus(_A)
_RcDhcp6SnoopingBindMac_Type=MacAddress
_RcDhcp6SnoopingBindMac_Object=MibTableColumn
rcDhcp6SnoopingBindMac=_RcDhcp6SnoopingBindMac_Object((1,3,6,1,4,1,8886,6,1,23,1,2,5,1,2),_RcDhcp6SnoopingBindMac_Type())
rcDhcp6SnoopingBindMac.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcp6SnoopingBindMac.setStatus(_A)
_RcDhcp6SnoopingBindLease_Type=Unsigned32
_RcDhcp6SnoopingBindLease_Object=MibTableColumn
rcDhcp6SnoopingBindLease=_RcDhcp6SnoopingBindLease_Object((1,3,6,1,4,1,8886,6,1,23,1,2,5,1,3),_RcDhcp6SnoopingBindLease_Type())
rcDhcp6SnoopingBindLease.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcp6SnoopingBindLease.setStatus(_A)
_RcDhcp6SnoopingBindVlan_Type=Integer32
_RcDhcp6SnoopingBindVlan_Object=MibTableColumn
rcDhcp6SnoopingBindVlan=_RcDhcp6SnoopingBindVlan_Object((1,3,6,1,4,1,8886,6,1,23,1,2,5,1,4),_RcDhcp6SnoopingBindVlan_Type())
rcDhcp6SnoopingBindVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcp6SnoopingBindVlan.setStatus(_A)
_RcDhcp6SnoopingBindPort_Type=Integer32
_RcDhcp6SnoopingBindPort_Object=MibTableColumn
rcDhcp6SnoopingBindPort=_RcDhcp6SnoopingBindPort_Object((1,3,6,1,4,1,8886,6,1,23,1,2,5,1,5),_RcDhcp6SnoopingBindPort_Type())
rcDhcp6SnoopingBindPort.setMaxAccess(_B)
if mibBuilder.loadTexts:rcDhcp6SnoopingBindPort.setStatus(_A)
_RcDhcp4SnoopingOptionGroup_ObjectIdentity=ObjectIdentity
rcDhcp4SnoopingOptionGroup=_RcDhcp4SnoopingOptionGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,23,1,3))
class _RcDhcpSnoopingOptionList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_RcDhcpSnoopingOptionList_Type.__name__=_H
_RcDhcpSnoopingOptionList_Object=MibScalar
rcDhcpSnoopingOptionList=_RcDhcpSnoopingOptionList_Object((1,3,6,1,4,1,8886,6,1,23,1,3,1),_RcDhcpSnoopingOptionList_Type())
rcDhcpSnoopingOptionList.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpSnoopingOptionList.setStatus(_A)
_RcDhcp6SnoopingOptionGroup_ObjectIdentity=ObjectIdentity
rcDhcp6SnoopingOptionGroup=_RcDhcp6SnoopingOptionGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,23,1,4))
class _RcDhcp6SnoopingOptionList_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(32,32));fixedLength=32
_RcDhcp6SnoopingOptionList_Type.__name__=_H
_RcDhcp6SnoopingOptionList_Object=MibScalar
rcDhcp6SnoopingOptionList=_RcDhcp6SnoopingOptionList_Object((1,3,6,1,4,1,8886,6,1,23,1,4,1),_RcDhcp6SnoopingOptionList_Type())
rcDhcp6SnoopingOptionList.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcp6SnoopingOptionList.setStatus(_A)
_RcDhcpSnoopingBindSaveGroup_ObjectIdentity=ObjectIdentity
rcDhcpSnoopingBindSaveGroup=_RcDhcpSnoopingBindSaveGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,23,1,5))
class _RcDhcpSnoopingBindSaveEnable_Type(EnableVar):defaultValue=2
_RcDhcpSnoopingBindSaveEnable_Type.__name__=_F
_RcDhcpSnoopingBindSaveEnable_Object=MibScalar
rcDhcpSnoopingBindSaveEnable=_RcDhcpSnoopingBindSaveEnable_Object((1,3,6,1,4,1,8886,6,1,23,1,5,1),_RcDhcpSnoopingBindSaveEnable_Type())
rcDhcpSnoopingBindSaveEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpSnoopingBindSaveEnable.setStatus(_A)
class _RcDhcpSnoopingBindSaveWriteDelay_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(60,2147483647))
_RcDhcpSnoopingBindSaveWriteDelay_Type.__name__=_D
_RcDhcpSnoopingBindSaveWriteDelay_Object=MibScalar
rcDhcpSnoopingBindSaveWriteDelay=_RcDhcpSnoopingBindSaveWriteDelay_Object((1,3,6,1,4,1,8886,6,1,23,1,5,2),_RcDhcpSnoopingBindSaveWriteDelay_Type())
rcDhcpSnoopingBindSaveWriteDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:rcDhcpSnoopingBindSaveWriteDelay.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'rcDhcpSnooping':rcDhcpSnooping,'rcDhcpSnoopingMibObjects':rcDhcpSnoopingMibObjects,'rcDhcpSnoopingGroup':rcDhcpSnoopingGroup,'rcDhcpSnoopingEnable':rcDhcpSnoopingEnable,'rcDhcpSnoopingPortTable':rcDhcpSnoopingPortTable,'rcDhcpSnoopingPortEntry':rcDhcpSnoopingPortEntry,_I:rcDhcpSnoopingPortIndex,'rcDhcpSnoopingPortEnable':rcDhcpSnoopingPortEnable,'rcDhcpSnoopingPortTrust':rcDhcpSnoopingPortTrust,'rcDhcpSnoopingBindCurrentRows':rcDhcpSnoopingBindCurrentRows,'rcDhcpSnoopingBindHistoryMaxRows':rcDhcpSnoopingBindHistoryMaxRows,'rcDhcpSnoopingBindTable':rcDhcpSnoopingBindTable,'rcDhcpSnoopingBindEntry':rcDhcpSnoopingBindEntry,_L:rcDhcpSnoopingBindIp,'rcDhcpSnoopingBindMac':rcDhcpSnoopingBindMac,'rcDhcpSnoopingBindLease':rcDhcpSnoopingBindLease,'rcDhcpSnoopingBindVlan':rcDhcpSnoopingBindVlan,'rcDhcpSnoopingBindPort':rcDhcpSnoopingBindPort,'rcDhcp6SnoopingGroup':rcDhcp6SnoopingGroup,'rcDhcp6SnoopingEnable':rcDhcp6SnoopingEnable,'rcDhcp6SnoopingPortTable':rcDhcp6SnoopingPortTable,'rcDhcp6SnoopingPortEntry':rcDhcp6SnoopingPortEntry,_M:rcDhcp6SnoopingPortIndex,'rcDhcp6SnoopingPortEnable':rcDhcp6SnoopingPortEnable,'rcDhcp6SnoopingPortTrust':rcDhcp6SnoopingPortTrust,'rcDhcp6SnoopingBindCurrentRows':rcDhcp6SnoopingBindCurrentRows,'rcDhcp6SnoopingBindHistoryMaxRows':rcDhcp6SnoopingBindHistoryMaxRows,'rcDhcp6SnoopingBindTable':rcDhcp6SnoopingBindTable,'rcDhcp6SnoopingBindEntry':rcDhcp6SnoopingBindEntry,_N:rcDhcp6SnoopingBindIp,'rcDhcp6SnoopingBindMac':rcDhcp6SnoopingBindMac,'rcDhcp6SnoopingBindLease':rcDhcp6SnoopingBindLease,'rcDhcp6SnoopingBindVlan':rcDhcp6SnoopingBindVlan,'rcDhcp6SnoopingBindPort':rcDhcp6SnoopingBindPort,'rcDhcp4SnoopingOptionGroup':rcDhcp4SnoopingOptionGroup,'rcDhcpSnoopingOptionList':rcDhcpSnoopingOptionList,'rcDhcp6SnoopingOptionGroup':rcDhcp6SnoopingOptionGroup,'rcDhcp6SnoopingOptionList':rcDhcp6SnoopingOptionList,'rcDhcpSnoopingBindSaveGroup':rcDhcpSnoopingBindSaveGroup,'rcDhcpSnoopingBindSaveEnable':rcDhcpSnoopingBindSaveEnable,'rcDhcpSnoopingBindSaveWriteDelay':rcDhcpSnoopingBindSaveWriteDelay})