_H='fsWanFpmResultsLinkQuality'
_G='fsWanFpmResultsSessStatus'
_F='reserved'
_E='fsWanFpmResultsIfIndex'
_D='Integer32'
_C='FS-WAN-FPM-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
IfIndex,=mibBuilder.importSymbols('FS-TC','IfIndex')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','PhysAddress','RowStatus','TextualConvention')
fsWanFpmMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,153))
if mibBuilder.loadTexts:fsWanFpmMIB.setRevisions(('2017-01-20 00:00',))
_FsWanFpmMIBObjects_ObjectIdentity=ObjectIdentity
fsWanFpmMIBObjects=_FsWanFpmMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,153,1))
_FsWanFpmResultsTable_Object=MibTable
fsWanFpmResultsTable=_FsWanFpmResultsTable_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1))
if mibBuilder.loadTexts:fsWanFpmResultsTable.setStatus(_A)
_FsWanFpmResultsEntry_Object=MibTableRow
fsWanFpmResultsEntry=_FsWanFpmResultsEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1))
fsWanFpmResultsEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:fsWanFpmResultsEntry.setStatus(_A)
_FsWanFpmResultsIfIndex_Type=IfIndex
_FsWanFpmResultsIfIndex_Object=MibTableColumn
fsWanFpmResultsIfIndex=_FsWanFpmResultsIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,1),_FsWanFpmResultsIfIndex_Type())
fsWanFpmResultsIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsIfIndex.setStatus(_A)
class _FsWanFpmResultsMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('passive',1),('active',2)))
_FsWanFpmResultsMode_Type.__name__=_D
_FsWanFpmResultsMode_Object=MibTableColumn
fsWanFpmResultsMode=_FsWanFpmResultsMode_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,2),_FsWanFpmResultsMode_Type())
fsWanFpmResultsMode.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsMode.setStatus(_A)
_FsWanFpmResultsPeerIp_Type=InetAddress
_FsWanFpmResultsPeerIp_Object=MibTableColumn
fsWanFpmResultsPeerIp=_FsWanFpmResultsPeerIp_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,3),_FsWanFpmResultsPeerIp_Type())
fsWanFpmResultsPeerIp.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsPeerIp.setStatus(_A)
_FsWanFpmResultsNetworkAF_Type=InetAddressType
_FsWanFpmResultsNetworkAF_Object=MibTableColumn
fsWanFpmResultsNetworkAF=_FsWanFpmResultsNetworkAF_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,4),_FsWanFpmResultsNetworkAF_Type())
fsWanFpmResultsNetworkAF.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsNetworkAF.setStatus(_A)
class _FsWanFpmResultsSessStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),(_F,3)))
_FsWanFpmResultsSessStatus_Type.__name__=_D
_FsWanFpmResultsSessStatus_Object=MibTableColumn
fsWanFpmResultsSessStatus=_FsWanFpmResultsSessStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,5),_FsWanFpmResultsSessStatus_Type())
fsWanFpmResultsSessStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsSessStatus.setStatus(_A)
class _FsWanFpmResultsLinkQuality_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('well',1),('worse',2),(_F,3)))
_FsWanFpmResultsLinkQuality_Type.__name__=_D
_FsWanFpmResultsLinkQuality_Object=MibTableColumn
fsWanFpmResultsLinkQuality=_FsWanFpmResultsLinkQuality_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,6),_FsWanFpmResultsLinkQuality_Type())
fsWanFpmResultsLinkQuality.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsLinkQuality.setStatus(_A)
class _FsWanFpmResultsWorseAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('forward',1),('unforward',2)))
_FsWanFpmResultsWorseAction_Type.__name__=_D
_FsWanFpmResultsWorseAction_Object=MibTableColumn
fsWanFpmResultsWorseAction=_FsWanFpmResultsWorseAction_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,7),_FsWanFpmResultsWorseAction_Type())
fsWanFpmResultsWorseAction.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsWorseAction.setStatus(_A)
_FsWanFpmResultsRTT_Type=Unsigned32
_FsWanFpmResultsRTT_Object=MibTableColumn
fsWanFpmResultsRTT=_FsWanFpmResultsRTT_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,8),_FsWanFpmResultsRTT_Type())
fsWanFpmResultsRTT.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsRTT.setStatus(_A)
_FsWanFpmResultsJitter_Type=Unsigned32
_FsWanFpmResultsJitter_Object=MibTableColumn
fsWanFpmResultsJitter=_FsWanFpmResultsJitter_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,9),_FsWanFpmResultsJitter_Type())
fsWanFpmResultsJitter.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsJitter.setStatus(_A)
_FsWanFpmResultsUpDroprate_Type=Unsigned32
_FsWanFpmResultsUpDroprate_Object=MibTableColumn
fsWanFpmResultsUpDroprate=_FsWanFpmResultsUpDroprate_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,10),_FsWanFpmResultsUpDroprate_Type())
fsWanFpmResultsUpDroprate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsUpDroprate.setStatus(_A)
_FsWanFpmResultsDownDroprate_Type=Unsigned32
_FsWanFpmResultsDownDroprate_Object=MibTableColumn
fsWanFpmResultsDownDroprate=_FsWanFpmResultsDownDroprate_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,11),_FsWanFpmResultsDownDroprate_Type())
fsWanFpmResultsDownDroprate.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsDownDroprate.setStatus(_A)
_FsWanFpmResultsByteTxSpeed_Type=Unsigned32
_FsWanFpmResultsByteTxSpeed_Object=MibTableColumn
fsWanFpmResultsByteTxSpeed=_FsWanFpmResultsByteTxSpeed_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,12),_FsWanFpmResultsByteTxSpeed_Type())
fsWanFpmResultsByteTxSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsByteTxSpeed.setStatus(_A)
_FsWanFpmResultsByteRxSpeed_Type=Unsigned32
_FsWanFpmResultsByteRxSpeed_Object=MibTableColumn
fsWanFpmResultsByteRxSpeed=_FsWanFpmResultsByteRxSpeed_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,13),_FsWanFpmResultsByteRxSpeed_Type())
fsWanFpmResultsByteRxSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsByteRxSpeed.setStatus(_A)
_FsWanFpmResultsPktsTxSpeed_Type=Unsigned32
_FsWanFpmResultsPktsTxSpeed_Object=MibTableColumn
fsWanFpmResultsPktsTxSpeed=_FsWanFpmResultsPktsTxSpeed_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,14),_FsWanFpmResultsPktsTxSpeed_Type())
fsWanFpmResultsPktsTxSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsPktsTxSpeed.setStatus(_A)
_FsWanFpmResultsPktsRxSpeed_Type=Unsigned32
_FsWanFpmResultsPktsRxSpeed_Object=MibTableColumn
fsWanFpmResultsPktsRxSpeed=_FsWanFpmResultsPktsRxSpeed_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,15),_FsWanFpmResultsPktsRxSpeed_Type())
fsWanFpmResultsPktsRxSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsPktsRxSpeed.setStatus(_A)
_FsWanFpmResultsCresteTime_Type=DateAndTime
_FsWanFpmResultsCresteTime_Object=MibTableColumn
fsWanFpmResultsCresteTime=_FsWanFpmResultsCresteTime_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,16),_FsWanFpmResultsCresteTime_Type())
fsWanFpmResultsCresteTime.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsCresteTime.setStatus(_A)
class _FsWanFpmResultsTrapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('getPeriodResult',1),('getTickResult',2),(_F,3)))
_FsWanFpmResultsTrapType_Type.__name__=_D
_FsWanFpmResultsTrapType_Object=MibTableColumn
fsWanFpmResultsTrapType=_FsWanFpmResultsTrapType_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,17),_FsWanFpmResultsTrapType_Type())
fsWanFpmResultsTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsTrapType.setStatus(_A)
_FsWanFpmResultsSessId_Type=Unsigned32
_FsWanFpmResultsSessId_Object=MibTableColumn
fsWanFpmResultsSessId=_FsWanFpmResultsSessId_Object((1,3,6,1,4,1,52642,1,1,10,2,153,1,1,1,18),_FsWanFpmResultsSessId_Type())
fsWanFpmResultsSessId.setMaxAccess(_B)
if mibBuilder.loadTexts:fsWanFpmResultsSessId.setStatus(_A)
_FsWanFpmMonitor_ObjectIdentity=ObjectIdentity
fsWanFpmMonitor=_FsWanFpmMonitor_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,153,2))
_FsWanFpmMonitorTRAP_ObjectIdentity=ObjectIdentity
fsWanFpmMonitorTRAP=_FsWanFpmMonitorTRAP_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,153,2,1))
_FsWanFpmNotifications_ObjectIdentity=ObjectIdentity
fsWanFpmNotifications=_FsWanFpmNotifications_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,153,2,1,1))
fsWanFpmLqWell=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,153,2,1,1,1))
fsWanFpmLqWell.setObjects(*((_C,_E),(_C,_G),(_C,_H)))
if mibBuilder.loadTexts:fsWanFpmLqWell.setStatus(_A)
fsWanFpmLqBad=NotificationType((1,3,6,1,4,1,52642,1,1,10,2,153,2,1,1,2))
fsWanFpmLqBad.setObjects(*((_C,_E),(_C,_G),(_C,_H)))
if mibBuilder.loadTexts:fsWanFpmLqBad.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'fsWanFpmMIB':fsWanFpmMIB,'fsWanFpmMIBObjects':fsWanFpmMIBObjects,'fsWanFpmResultsTable':fsWanFpmResultsTable,'fsWanFpmResultsEntry':fsWanFpmResultsEntry,_E:fsWanFpmResultsIfIndex,'fsWanFpmResultsMode':fsWanFpmResultsMode,'fsWanFpmResultsPeerIp':fsWanFpmResultsPeerIp,'fsWanFpmResultsNetworkAF':fsWanFpmResultsNetworkAF,_G:fsWanFpmResultsSessStatus,_H:fsWanFpmResultsLinkQuality,'fsWanFpmResultsWorseAction':fsWanFpmResultsWorseAction,'fsWanFpmResultsRTT':fsWanFpmResultsRTT,'fsWanFpmResultsJitter':fsWanFpmResultsJitter,'fsWanFpmResultsUpDroprate':fsWanFpmResultsUpDroprate,'fsWanFpmResultsDownDroprate':fsWanFpmResultsDownDroprate,'fsWanFpmResultsByteTxSpeed':fsWanFpmResultsByteTxSpeed,'fsWanFpmResultsByteRxSpeed':fsWanFpmResultsByteRxSpeed,'fsWanFpmResultsPktsTxSpeed':fsWanFpmResultsPktsTxSpeed,'fsWanFpmResultsPktsRxSpeed':fsWanFpmResultsPktsRxSpeed,'fsWanFpmResultsCresteTime':fsWanFpmResultsCresteTime,'fsWanFpmResultsTrapType':fsWanFpmResultsTrapType,'fsWanFpmResultsSessId':fsWanFpmResultsSessId,'fsWanFpmMonitor':fsWanFpmMonitor,'fsWanFpmMonitorTRAP':fsWanFpmMonitorTRAP,'fsWanFpmNotifications':fsWanFpmNotifications,'fsWanFpmLqWell':fsWanFpmLqWell,'fsWanFpmLqBad':fsWanFpmLqBad})