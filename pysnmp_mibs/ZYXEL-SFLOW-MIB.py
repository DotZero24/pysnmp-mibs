_L='zySflowPortCollectorIpAddress'
_K='zySflowPortCollectorIpAddressType'
_J='read-create'
_I='zySflowCollectorIpAddress'
_H='zySflowCollectorIpAddressType'
_G='read-only'
_F='dot1dBasePort'
_E='BRIDGE-MIB'
_D='not-accessible'
_C='ZYXEL-SFLOW-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_E,_F)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelSflow=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,75))
_ZyxelSflowSetup_ObjectIdentity=ObjectIdentity
zyxelSflowSetup=_ZyxelSflowSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,75,1))
_ZySflowState_Type=EnabledStatus
_ZySflowState_Object=MibScalar
zySflowState=_ZySflowState_Object((1,3,6,1,4,1,890,1,15,3,75,1,1),_ZySflowState_Type())
zySflowState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySflowState.setStatus(_A)
_ZySflowMaxNumberOfCollectors_Type=Integer32
_ZySflowMaxNumberOfCollectors_Object=MibScalar
zySflowMaxNumberOfCollectors=_ZySflowMaxNumberOfCollectors_Object((1,3,6,1,4,1,890,1,15,3,75,1,2),_ZySflowMaxNumberOfCollectors_Type())
zySflowMaxNumberOfCollectors.setMaxAccess(_G)
if mibBuilder.loadTexts:zySflowMaxNumberOfCollectors.setStatus(_A)
_ZyxelSflowCollectorTable_Object=MibTable
zyxelSflowCollectorTable=_ZyxelSflowCollectorTable_Object((1,3,6,1,4,1,890,1,15,3,75,1,3))
if mibBuilder.loadTexts:zyxelSflowCollectorTable.setStatus(_A)
_ZyxelSflowCollectorEntry_Object=MibTableRow
zyxelSflowCollectorEntry=_ZyxelSflowCollectorEntry_Object((1,3,6,1,4,1,890,1,15,3,75,1,3,1))
zyxelSflowCollectorEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:zyxelSflowCollectorEntry.setStatus(_A)
_ZySflowCollectorIpAddressType_Type=InetAddressType
_ZySflowCollectorIpAddressType_Object=MibTableColumn
zySflowCollectorIpAddressType=_ZySflowCollectorIpAddressType_Object((1,3,6,1,4,1,890,1,15,3,75,1,3,1,1),_ZySflowCollectorIpAddressType_Type())
zySflowCollectorIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:zySflowCollectorIpAddressType.setStatus(_A)
_ZySflowCollectorIpAddress_Type=InetAddress
_ZySflowCollectorIpAddress_Object=MibTableColumn
zySflowCollectorIpAddress=_ZySflowCollectorIpAddress_Object((1,3,6,1,4,1,890,1,15,3,75,1,3,1,2),_ZySflowCollectorIpAddress_Type())
zySflowCollectorIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zySflowCollectorIpAddress.setStatus(_A)
_ZySflowCollectorUdpPort_Type=Integer32
_ZySflowCollectorUdpPort_Object=MibTableColumn
zySflowCollectorUdpPort=_ZySflowCollectorUdpPort_Object((1,3,6,1,4,1,890,1,15,3,75,1,3,1,3),_ZySflowCollectorUdpPort_Type())
zySflowCollectorUdpPort.setMaxAccess(_B)
if mibBuilder.loadTexts:zySflowCollectorUdpPort.setStatus(_A)
_ZySflowCollectorRowStatus_Type=RowStatus
_ZySflowCollectorRowStatus_Object=MibTableColumn
zySflowCollectorRowStatus=_ZySflowCollectorRowStatus_Object((1,3,6,1,4,1,890,1,15,3,75,1,3,1,4),_ZySflowCollectorRowStatus_Type())
zySflowCollectorRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:zySflowCollectorRowStatus.setStatus(_A)
_ZyxelSflowPortTable_Object=MibTable
zyxelSflowPortTable=_ZyxelSflowPortTable_Object((1,3,6,1,4,1,890,1,15,3,75,1,4))
if mibBuilder.loadTexts:zyxelSflowPortTable.setStatus(_A)
_ZyxelSflowPortEntry_Object=MibTableRow
zyxelSflowPortEntry=_ZyxelSflowPortEntry_Object((1,3,6,1,4,1,890,1,15,3,75,1,4,1))
zyxelSflowPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zyxelSflowPortEntry.setStatus(_A)
_ZySflowPortState_Type=EnabledStatus
_ZySflowPortState_Object=MibTableColumn
zySflowPortState=_ZySflowPortState_Object((1,3,6,1,4,1,890,1,15,3,75,1,4,1,1),_ZySflowPortState_Type())
zySflowPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:zySflowPortState.setStatus(_A)
_ZySflowMaxNumberOfPortCollectors_Type=Integer32
_ZySflowMaxNumberOfPortCollectors_Object=MibScalar
zySflowMaxNumberOfPortCollectors=_ZySflowMaxNumberOfPortCollectors_Object((1,3,6,1,4,1,890,1,15,3,75,1,5),_ZySflowMaxNumberOfPortCollectors_Type())
zySflowMaxNumberOfPortCollectors.setMaxAccess(_G)
if mibBuilder.loadTexts:zySflowMaxNumberOfPortCollectors.setStatus(_A)
_ZyxelSflowPortCollectorTable_Object=MibTable
zyxelSflowPortCollectorTable=_ZyxelSflowPortCollectorTable_Object((1,3,6,1,4,1,890,1,15,3,75,1,6))
if mibBuilder.loadTexts:zyxelSflowPortCollectorTable.setStatus(_A)
_ZyxelSflowPortCollectorEntry_Object=MibTableRow
zyxelSflowPortCollectorEntry=_ZyxelSflowPortCollectorEntry_Object((1,3,6,1,4,1,890,1,15,3,75,1,6,1))
zyxelSflowPortCollectorEntry.setIndexNames((0,_E,_F),(0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:zyxelSflowPortCollectorEntry.setStatus(_A)
_ZySflowPortCollectorIpAddressType_Type=InetAddressType
_ZySflowPortCollectorIpAddressType_Object=MibTableColumn
zySflowPortCollectorIpAddressType=_ZySflowPortCollectorIpAddressType_Object((1,3,6,1,4,1,890,1,15,3,75,1,6,1,1),_ZySflowPortCollectorIpAddressType_Type())
zySflowPortCollectorIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:zySflowPortCollectorIpAddressType.setStatus(_A)
_ZySflowPortCollectorIpAddress_Type=InetAddress
_ZySflowPortCollectorIpAddress_Object=MibTableColumn
zySflowPortCollectorIpAddress=_ZySflowPortCollectorIpAddress_Object((1,3,6,1,4,1,890,1,15,3,75,1,6,1,2),_ZySflowPortCollectorIpAddress_Type())
zySflowPortCollectorIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:zySflowPortCollectorIpAddress.setStatus(_A)
_ZySflowPortCollectorSampleRate_Type=Integer32
_ZySflowPortCollectorSampleRate_Object=MibTableColumn
zySflowPortCollectorSampleRate=_ZySflowPortCollectorSampleRate_Object((1,3,6,1,4,1,890,1,15,3,75,1,6,1,3),_ZySflowPortCollectorSampleRate_Type())
zySflowPortCollectorSampleRate.setMaxAccess(_B)
if mibBuilder.loadTexts:zySflowPortCollectorSampleRate.setStatus(_A)
_ZySflowPortCollectorPollInterval_Type=Integer32
_ZySflowPortCollectorPollInterval_Object=MibTableColumn
zySflowPortCollectorPollInterval=_ZySflowPortCollectorPollInterval_Object((1,3,6,1,4,1,890,1,15,3,75,1,6,1,4),_ZySflowPortCollectorPollInterval_Type())
zySflowPortCollectorPollInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:zySflowPortCollectorPollInterval.setStatus(_A)
_ZySflowPortCollectorRowStatus_Type=RowStatus
_ZySflowPortCollectorRowStatus_Object=MibTableColumn
zySflowPortCollectorRowStatus=_ZySflowPortCollectorRowStatus_Object((1,3,6,1,4,1,890,1,15,3,75,1,6,1,5),_ZySflowPortCollectorRowStatus_Type())
zySflowPortCollectorRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:zySflowPortCollectorRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelSflow':zyxelSflow,'zyxelSflowSetup':zyxelSflowSetup,'zySflowState':zySflowState,'zySflowMaxNumberOfCollectors':zySflowMaxNumberOfCollectors,'zyxelSflowCollectorTable':zyxelSflowCollectorTable,'zyxelSflowCollectorEntry':zyxelSflowCollectorEntry,_H:zySflowCollectorIpAddressType,_I:zySflowCollectorIpAddress,'zySflowCollectorUdpPort':zySflowCollectorUdpPort,'zySflowCollectorRowStatus':zySflowCollectorRowStatus,'zyxelSflowPortTable':zyxelSflowPortTable,'zyxelSflowPortEntry':zyxelSflowPortEntry,'zySflowPortState':zySflowPortState,'zySflowMaxNumberOfPortCollectors':zySflowMaxNumberOfPortCollectors,'zyxelSflowPortCollectorTable':zyxelSflowPortCollectorTable,'zyxelSflowPortCollectorEntry':zyxelSflowPortCollectorEntry,_K:zySflowPortCollectorIpAddressType,_L:zySflowPortCollectorIpAddress,'zySflowPortCollectorSampleRate':zySflowPortCollectorSampleRate,'zySflowPortCollectorPollInterval':zySflowPortCollectorPollInterval,'zySflowPortCollectorRowStatus':zySflowPortCollectorRowStatus})