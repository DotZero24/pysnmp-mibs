_O='rlOpcActionCaptureName'
_N='rlOpcInterfaceIfIndex'
_M='rlOpcInterfaceCaptureName'
_L='inactive'
_K='active'
_J='rlOpcName'
_I='OctetString'
_H='read-create'
_G='CISCOSB-OPC-MIB'
_F='DisplayString'
_E='read-only'
_D='Unsigned32'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_I,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
switch001,=mibBuilder.importSymbols('CISCOSB-MIB','switch001')
InterfaceIndexOrZero,=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
rlOpc=ModuleIdentity((1,3,6,1,4,1,9,6,1,101,248))
if mibBuilder.loadTexts:rlOpc.setRevisions(('2024-01-10 00:00',))
_RlOpcCapturePointTable_Object=MibTable
rlOpcCapturePointTable=_RlOpcCapturePointTable_Object((1,3,6,1,4,1,9,6,1,101,248,1))
if mibBuilder.loadTexts:rlOpcCapturePointTable.setStatus(_A)
_RlOpcCapturePointEntry_Object=MibTableRow
rlOpcCapturePointEntry=_RlOpcCapturePointEntry_Object((1,3,6,1,4,1,9,6,1,101,248,1,1))
rlOpcCapturePointEntry.setIndexNames((0,_G,_J))
if mibBuilder.loadTexts:rlOpcCapturePointEntry.setStatus(_A)
class _RlOpcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlOpcName_Type.__name__=_F
_RlOpcName_Object=MibTableColumn
rlOpcName=_RlOpcName_Object((1,3,6,1,4,1,9,6,1,101,248,1,1,1),_RlOpcName_Type())
rlOpcName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpcName.setStatus(_A)
class _RlOpcBufferType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('linear',1),('circular',2)))
_RlOpcBufferType_Type.__name__=_C
_RlOpcBufferType_Object=MibTableColumn
rlOpcBufferType=_RlOpcBufferType_Object((1,3,6,1,4,1,9,6,1,101,248,1,1,2),_RlOpcBufferType_Type())
rlOpcBufferType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpcBufferType.setStatus(_A)
_RlOpcBufferSize_Type=Unsigned32
_RlOpcBufferSize_Object=MibTableColumn
rlOpcBufferSize=_RlOpcBufferSize_Object((1,3,6,1,4,1,9,6,1,101,248,1,1,3),_RlOpcBufferSize_Type())
rlOpcBufferSize.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpcBufferSize.setStatus(_A)
class _RlOpcBufferUsed_Type(Unsigned32):defaultValue=0
_RlOpcBufferUsed_Type.__name__=_D
_RlOpcBufferUsed_Object=MibTableColumn
rlOpcBufferUsed=_RlOpcBufferUsed_Object((1,3,6,1,4,1,9,6,1,101,248,1,1,4),_RlOpcBufferUsed_Type())
rlOpcBufferUsed.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOpcBufferUsed.setStatus(_A)
class _RlOpcBufferPacketNum_Type(Unsigned32):defaultValue=0
_RlOpcBufferPacketNum_Type.__name__=_D
_RlOpcBufferPacketNum_Object=MibTableColumn
rlOpcBufferPacketNum=_RlOpcBufferPacketNum_Object((1,3,6,1,4,1,9,6,1,101,248,1,1,5),_RlOpcBufferPacketNum_Type())
rlOpcBufferPacketNum.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOpcBufferPacketNum.setStatus(_A)
class _RlOpcBufferPacketsDropped_Type(Unsigned32):defaultValue=0
_RlOpcBufferPacketsDropped_Type.__name__=_D
_RlOpcBufferPacketsDropped_Object=MibTableColumn
rlOpcBufferPacketsDropped=_RlOpcBufferPacketsDropped_Object((1,3,6,1,4,1,9,6,1,101,248,1,1,6),_RlOpcBufferPacketsDropped_Type())
rlOpcBufferPacketsDropped.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOpcBufferPacketsDropped.setStatus(_A)
class _RlOpcBufferPacketsPerSecond_Type(Unsigned32):defaultValue=0
_RlOpcBufferPacketsPerSecond_Type.__name__=_D
_RlOpcBufferPacketsPerSecond_Object=MibTableColumn
rlOpcBufferPacketsPerSecond=_RlOpcBufferPacketsPerSecond_Object((1,3,6,1,4,1,9,6,1,101,248,1,1,7),_RlOpcBufferPacketsPerSecond_Type())
rlOpcBufferPacketsPerSecond.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOpcBufferPacketsPerSecond.setStatus(_A)
class _RlOpcFilterType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('match-none',0),('match-any',1),('match-access-list',2)))
_RlOpcFilterType_Type.__name__=_C
_RlOpcFilterType_Object=MibTableColumn
rlOpcFilterType=_RlOpcFilterType_Object((1,3,6,1,4,1,9,6,1,101,248,1,1,8),_RlOpcFilterType_Type())
rlOpcFilterType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpcFilterType.setStatus(_A)
class _RlOpcFilterAclName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_RlOpcFilterAclName_Type.__name__=_F
_RlOpcFilterAclName_Object=MibTableColumn
rlOpcFilterAclName=_RlOpcFilterAclName_Object((1,3,6,1,4,1,9,6,1,101,248,1,1,9),_RlOpcFilterAclName_Type())
rlOpcFilterAclName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpcFilterAclName.setStatus(_A)
class _RlOpcLimitDuration_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_RlOpcLimitDuration_Type.__name__=_D
_RlOpcLimitDuration_Object=MibTableColumn
rlOpcLimitDuration=_RlOpcLimitDuration_Object((1,3,6,1,4,1,9,6,1,101,248,1,1,10),_RlOpcLimitDuration_Type())
rlOpcLimitDuration.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpcLimitDuration.setStatus(_A)
if mibBuilder.loadTexts:rlOpcLimitDuration.setUnits('seconds')
class _RlOpcLimitNumOfPackets_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000000))
_RlOpcLimitNumOfPackets_Type.__name__=_D
_RlOpcLimitNumOfPackets_Object=MibTableColumn
rlOpcLimitNumOfPackets=_RlOpcLimitNumOfPackets_Object((1,3,6,1,4,1,9,6,1,101,248,1,1,11),_RlOpcLimitNumOfPackets_Type())
rlOpcLimitNumOfPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpcLimitNumOfPackets.setStatus(_A)
class _RlOpcLimitMaxPacketLen_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,9500),ValueRangeConstraint(0,0))
_RlOpcLimitMaxPacketLen_Type.__name__=_D
_RlOpcLimitMaxPacketLen_Object=MibTableColumn
rlOpcLimitMaxPacketLen=_RlOpcLimitMaxPacketLen_Object((1,3,6,1,4,1,9,6,1,101,248,1,1,12),_RlOpcLimitMaxPacketLen_Type())
rlOpcLimitMaxPacketLen.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpcLimitMaxPacketLen.setStatus(_A)
class _RlOpcState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_RlOpcState_Type.__name__=_C
_RlOpcState_Object=MibTableColumn
rlOpcState=_RlOpcState_Object((1,3,6,1,4,1,9,6,1,101,248,1,1,13),_RlOpcState_Type())
rlOpcState.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOpcState.setStatus(_A)
_RlOpcCapturePointRowStatus_Type=RowStatus
_RlOpcCapturePointRowStatus_Object=MibTableColumn
rlOpcCapturePointRowStatus=_RlOpcCapturePointRowStatus_Object((1,3,6,1,4,1,9,6,1,101,248,1,1,14),_RlOpcCapturePointRowStatus_Type())
rlOpcCapturePointRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:rlOpcCapturePointRowStatus.setStatus(_A)
_RlOpcInterfaceTable_Object=MibTable
rlOpcInterfaceTable=_RlOpcInterfaceTable_Object((1,3,6,1,4,1,9,6,1,101,248,2))
if mibBuilder.loadTexts:rlOpcInterfaceTable.setStatus(_A)
_RlOpcInterfaceEntry_Object=MibTableRow
rlOpcInterfaceEntry=_RlOpcInterfaceEntry_Object((1,3,6,1,4,1,9,6,1,101,248,2,1))
rlOpcInterfaceEntry.setIndexNames((0,_G,_M),(0,_G,_N))
if mibBuilder.loadTexts:rlOpcInterfaceEntry.setStatus(_A)
class _RlOpcInterfaceCaptureName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlOpcInterfaceCaptureName_Type.__name__=_F
_RlOpcInterfaceCaptureName_Object=MibTableColumn
rlOpcInterfaceCaptureName=_RlOpcInterfaceCaptureName_Object((1,3,6,1,4,1,9,6,1,101,248,2,1,1),_RlOpcInterfaceCaptureName_Type())
rlOpcInterfaceCaptureName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpcInterfaceCaptureName.setStatus(_A)
_RlOpcInterfaceIfIndex_Type=InterfaceIndexOrZero
_RlOpcInterfaceIfIndex_Object=MibTableColumn
rlOpcInterfaceIfIndex=_RlOpcInterfaceIfIndex_Object((1,3,6,1,4,1,9,6,1,101,248,2,1,2),_RlOpcInterfaceIfIndex_Type())
rlOpcInterfaceIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpcInterfaceIfIndex.setStatus(_A)
class _RlOpcInterfaceCaptureDirection_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('none',0),('in',1),('out',2),('both',3)))
_RlOpcInterfaceCaptureDirection_Type.__name__=_C
_RlOpcInterfaceCaptureDirection_Object=MibTableColumn
rlOpcInterfaceCaptureDirection=_RlOpcInterfaceCaptureDirection_Object((1,3,6,1,4,1,9,6,1,101,248,2,1,3),_RlOpcInterfaceCaptureDirection_Type())
rlOpcInterfaceCaptureDirection.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpcInterfaceCaptureDirection.setStatus(_A)
_RlOpcInterfaceRowStatus_Type=RowStatus
_RlOpcInterfaceRowStatus_Object=MibTableColumn
rlOpcInterfaceRowStatus=_RlOpcInterfaceRowStatus_Object((1,3,6,1,4,1,9,6,1,101,248,2,1,4),_RlOpcInterfaceRowStatus_Type())
rlOpcInterfaceRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:rlOpcInterfaceRowStatus.setStatus(_A)
_RlOpcActionTable_Object=MibTable
rlOpcActionTable=_RlOpcActionTable_Object((1,3,6,1,4,1,9,6,1,101,248,3))
if mibBuilder.loadTexts:rlOpcActionTable.setStatus(_A)
_RlOpcActionEntry_Object=MibTableRow
rlOpcActionEntry=_RlOpcActionEntry_Object((1,3,6,1,4,1,9,6,1,101,248,3,1))
rlOpcActionEntry.setIndexNames((0,_G,_O))
if mibBuilder.loadTexts:rlOpcActionEntry.setStatus(_A)
class _RlOpcActionCaptureName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_RlOpcActionCaptureName_Type.__name__=_F
_RlOpcActionCaptureName_Object=MibTableColumn
rlOpcActionCaptureName=_RlOpcActionCaptureName_Object((1,3,6,1,4,1,9,6,1,101,248,3,1,1),_RlOpcActionCaptureName_Type())
rlOpcActionCaptureName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpcActionCaptureName.setStatus(_A)
class _RlOpcExportDestLocationType_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('flash',0),('usb',1)))
_RlOpcExportDestLocationType_Type.__name__=_C
_RlOpcExportDestLocationType_Object=MibTableColumn
rlOpcExportDestLocationType=_RlOpcExportDestLocationType_Object((1,3,6,1,4,1,9,6,1,101,248,3,1,2),_RlOpcExportDestLocationType_Type())
rlOpcExportDestLocationType.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpcExportDestLocationType.setStatus(_A)
class _RlOpcExportFileName_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,160))
_RlOpcExportFileName_Type.__name__=_I
_RlOpcExportFileName_Object=MibTableColumn
rlOpcExportFileName=_RlOpcExportFileName_Object((1,3,6,1,4,1,9,6,1,101,248,3,1,3),_RlOpcExportFileName_Type())
rlOpcExportFileName.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpcExportFileName.setStatus(_A)
class _RlOpcAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('start',1),('stop',2),('export',3),('clear',4)))
_RlOpcAction_Type.__name__=_C
_RlOpcAction_Object=MibTableColumn
rlOpcAction=_RlOpcAction_Object((1,3,6,1,4,1,9,6,1,101,248,3,1,4),_RlOpcAction_Type())
rlOpcAction.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpcAction.setStatus(_A)
_RlOpcActionRowStatus_Type=RowStatus
_RlOpcActionRowStatus_Object=MibTableColumn
rlOpcActionRowStatus=_RlOpcActionRowStatus_Object((1,3,6,1,4,1,9,6,1,101,248,3,1,5),_RlOpcActionRowStatus_Type())
rlOpcActionRowStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:rlOpcActionRowStatus.setStatus(_A)
class _RlOpcCrashExportDestination_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('flash',0),('usb',1)))
_RlOpcCrashExportDestination_Type.__name__=_C
_RlOpcCrashExportDestination_Object=MibScalar
rlOpcCrashExportDestination=_RlOpcCrashExportDestination_Object((1,3,6,1,4,1,9,6,1,101,248,5),_RlOpcCrashExportDestination_Type())
rlOpcCrashExportDestination.setMaxAccess(_B)
if mibBuilder.loadTexts:rlOpcCrashExportDestination.setStatus(_A)
class _RlOpcOperState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_RlOpcOperState_Type.__name__=_C
_RlOpcOperState_Object=MibScalar
rlOpcOperState=_RlOpcOperState_Object((1,3,6,1,4,1,9,6,1,101,248,6),_RlOpcOperState_Type())
rlOpcOperState.setMaxAccess(_E)
if mibBuilder.loadTexts:rlOpcOperState.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'rlOpc':rlOpc,'rlOpcCapturePointTable':rlOpcCapturePointTable,'rlOpcCapturePointEntry':rlOpcCapturePointEntry,_J:rlOpcName,'rlOpcBufferType':rlOpcBufferType,'rlOpcBufferSize':rlOpcBufferSize,'rlOpcBufferUsed':rlOpcBufferUsed,'rlOpcBufferPacketNum':rlOpcBufferPacketNum,'rlOpcBufferPacketsDropped':rlOpcBufferPacketsDropped,'rlOpcBufferPacketsPerSecond':rlOpcBufferPacketsPerSecond,'rlOpcFilterType':rlOpcFilterType,'rlOpcFilterAclName':rlOpcFilterAclName,'rlOpcLimitDuration':rlOpcLimitDuration,'rlOpcLimitNumOfPackets':rlOpcLimitNumOfPackets,'rlOpcLimitMaxPacketLen':rlOpcLimitMaxPacketLen,'rlOpcState':rlOpcState,'rlOpcCapturePointRowStatus':rlOpcCapturePointRowStatus,'rlOpcInterfaceTable':rlOpcInterfaceTable,'rlOpcInterfaceEntry':rlOpcInterfaceEntry,_M:rlOpcInterfaceCaptureName,_N:rlOpcInterfaceIfIndex,'rlOpcInterfaceCaptureDirection':rlOpcInterfaceCaptureDirection,'rlOpcInterfaceRowStatus':rlOpcInterfaceRowStatus,'rlOpcActionTable':rlOpcActionTable,'rlOpcActionEntry':rlOpcActionEntry,_O:rlOpcActionCaptureName,'rlOpcExportDestLocationType':rlOpcExportDestLocationType,'rlOpcExportFileName':rlOpcExportFileName,'rlOpcAction':rlOpcAction,'rlOpcActionRowStatus':rlOpcActionRowStatus,'rlOpcCrashExportDestination':rlOpcCrashExportDestination,'rlOpcOperState':rlOpcOperState})