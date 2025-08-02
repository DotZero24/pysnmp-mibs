_Q='portEth2Status'
_P='portEth2Priority'
_O='tagEth2Status'
_N='tagEth2Priority'
_M='portEth1Status'
_L='portEth1Priority'
_K='tagEth1Status'
_J='tagEth1Priority'
_I='diffServEnable'
_H='diffServPriority'
_G='diffServValue'
_F='Integer32'
_E='w-4'
_D='w-8'
_C='QOS'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
radioConfig,=mibBuilder.importSymbols('ExaltComProducts','radioConfig')
EnableStatusT,QosTagT,VlanIdT=mibBuilder.importSymbols('ExaltComm','EnableStatusT','QosTagT','VlanIdT')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class QosPriorityT(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('priority0',0),('priority1',1),('priority2',2),('priority3',3)))
class QosModeT(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4,5,6)));namedValues=NamedValues(*(('disable',0),('qos-mode-802-1p',4),('qos-mode-diffserv',5),('qos-mode-port',6)))
class QosScheduleModeT(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('weighted-round-robin',0),('hybrid1-mode-3sp-2wrr-1wrr-0wrr',1),('hybrid2-mode-3sp-2sp-1wrr-0wrr',2),('strict-priority',3)))
class QosCos3WeightT(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(8,16,32)));namedValues=NamedValues(*((_D,8),('w-16',16),('w-32',32)))
class QosCos2WeightT(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(4,8,16)));namedValues=NamedValues(*((_E,4),(_D,8),('w-16',16)))
class QosCos1WeightT(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4,8)));namedValues=NamedValues(*(('w-2',2),(_E,4),(_D,8)))
class QosCos0WeightT(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,4)));namedValues=NamedValues(*(('w-1',1),('w-2',2),(_E,4)))
_AdvSystemConfig_ObjectIdentity=ObjectIdentity
advSystemConfig=_AdvSystemConfig_ObjectIdentity((1,3,6,1,4,1,25651,1,2,3,5))
if mibBuilder.loadTexts:advSystemConfig.setStatus(_A)
_ExtAirG2QoS_ObjectIdentity=ObjectIdentity
extAirG2QoS=_ExtAirG2QoS_ObjectIdentity((1,3,6,1,4,1,25651,1,2,3,5,8))
if mibBuilder.loadTexts:extAirG2QoS.setStatus(_A)
_QosDefaultQueue_Type=QosPriorityT
_QosDefaultQueue_Object=MibScalar
qosDefaultQueue=_QosDefaultQueue_Object((1,3,6,1,4,1,25651,1,2,3,5,8,1),_QosDefaultQueue_Type())
qosDefaultQueue.setMaxAccess(_B)
if mibBuilder.loadTexts:qosDefaultQueue.setStatus(_A)
_QosEth1Mode_Type=QosModeT
_QosEth1Mode_Object=MibScalar
qosEth1Mode=_QosEth1Mode_Object((1,3,6,1,4,1,25651,1,2,3,5,8,2),_QosEth1Mode_Type())
qosEth1Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:qosEth1Mode.setStatus(_A)
_QosEth2Mode_Type=QosModeT
_QosEth2Mode_Object=MibScalar
qosEth2Mode=_QosEth2Mode_Object((1,3,6,1,4,1,25651,1,2,3,5,8,3),_QosEth2Mode_Type())
qosEth2Mode.setMaxAccess(_B)
if mibBuilder.loadTexts:qosEth2Mode.setStatus(_A)
_QosDiffServList_Object=MibTable
qosDiffServList=_QosDiffServList_Object((1,3,6,1,4,1,25651,1,2,3,5,8,4))
if mibBuilder.loadTexts:qosDiffServList.setStatus(_A)
_QosDiffServEntry_Object=MibTableRow
qosDiffServEntry=_QosDiffServEntry_Object((1,3,6,1,4,1,25651,1,2,3,5,8,4,1))
qosDiffServEntry.setIndexNames((0,_C,_G),(0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:qosDiffServEntry.setStatus(_A)
class _DiffServValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_DiffServValue_Type.__name__=_F
_DiffServValue_Object=MibTableColumn
diffServValue=_DiffServValue_Object((1,3,6,1,4,1,25651,1,2,3,5,8,4,1,1),_DiffServValue_Type())
diffServValue.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServValue.setStatus(_A)
_DiffServPriority_Type=QosPriorityT
_DiffServPriority_Object=MibTableColumn
diffServPriority=_DiffServPriority_Object((1,3,6,1,4,1,25651,1,2,3,5,8,4,1,2),_DiffServPriority_Type())
diffServPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServPriority.setStatus(_A)
_DiffServEnable_Type=EnableStatusT
_DiffServEnable_Object=MibTableColumn
diffServEnable=_DiffServEnable_Object((1,3,6,1,4,1,25651,1,2,3,5,8,4,1,3),_DiffServEnable_Type())
diffServEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:diffServEnable.setStatus(_A)
_QosPortETH1Conf_ObjectIdentity=ObjectIdentity
qosPortETH1Conf=_QosPortETH1Conf_ObjectIdentity((1,3,6,1,4,1,25651,1,2,3,5,8,5))
_QosEth1m802dot1pList_Object=MibTable
qosEth1m802dot1pList=_QosEth1m802dot1pList_Object((1,3,6,1,4,1,25651,1,2,3,5,8,5,1))
if mibBuilder.loadTexts:qosEth1m802dot1pList.setStatus(_A)
_QosEth1m802dot1pEntry_Object=MibTableRow
qosEth1m802dot1pEntry=_QosEth1m802dot1pEntry_Object((1,3,6,1,4,1,25651,1,2,3,5,8,5,1,1))
qosEth1m802dot1pEntry.setIndexNames((0,_C,_J),(0,_C,_K))
if mibBuilder.loadTexts:qosEth1m802dot1pEntry.setStatus(_A)
_TagEth1Priority_Type=QosPriorityT
_TagEth1Priority_Object=MibTableColumn
tagEth1Priority=_TagEth1Priority_Object((1,3,6,1,4,1,25651,1,2,3,5,8,5,1,1,1),_TagEth1Priority_Type())
tagEth1Priority.setMaxAccess(_B)
if mibBuilder.loadTexts:tagEth1Priority.setStatus(_A)
_TagEth1Status_Type=EnableStatusT
_TagEth1Status_Object=MibTableColumn
tagEth1Status=_TagEth1Status_Object((1,3,6,1,4,1,25651,1,2,3,5,8,5,1,1,2),_TagEth1Status_Type())
tagEth1Status.setMaxAccess(_B)
if mibBuilder.loadTexts:tagEth1Status.setStatus(_A)
_QosEth1PortList_Object=MibTable
qosEth1PortList=_QosEth1PortList_Object((1,3,6,1,4,1,25651,1,2,3,5,8,5,2))
if mibBuilder.loadTexts:qosEth1PortList.setStatus(_A)
_QosEth1PortEntry_Object=MibTableRow
qosEth1PortEntry=_QosEth1PortEntry_Object((1,3,6,1,4,1,25651,1,2,3,5,8,5,2,1))
qosEth1PortEntry.setIndexNames((0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:qosEth1PortEntry.setStatus(_A)
_PortEth1Priority_Type=QosPriorityT
_PortEth1Priority_Object=MibTableColumn
portEth1Priority=_PortEth1Priority_Object((1,3,6,1,4,1,25651,1,2,3,5,8,5,2,1,1),_PortEth1Priority_Type())
portEth1Priority.setMaxAccess(_B)
if mibBuilder.loadTexts:portEth1Priority.setStatus(_A)
_PortEth1Status_Type=EnableStatusT
_PortEth1Status_Object=MibTableColumn
portEth1Status=_PortEth1Status_Object((1,3,6,1,4,1,25651,1,2,3,5,8,5,2,1,2),_PortEth1Status_Type())
portEth1Status.setMaxAccess(_B)
if mibBuilder.loadTexts:portEth1Status.setStatus(_A)
_QosPortETH2Conf_ObjectIdentity=ObjectIdentity
qosPortETH2Conf=_QosPortETH2Conf_ObjectIdentity((1,3,6,1,4,1,25651,1,2,3,5,8,6))
_QosEth2m802dot1pList_Object=MibTable
qosEth2m802dot1pList=_QosEth2m802dot1pList_Object((1,3,6,1,4,1,25651,1,2,3,5,8,6,1))
if mibBuilder.loadTexts:qosEth2m802dot1pList.setStatus(_A)
_QosEth2m802dot1pEntry_Object=MibTableRow
qosEth2m802dot1pEntry=_QosEth2m802dot1pEntry_Object((1,3,6,1,4,1,25651,1,2,3,5,8,6,1,1))
qosEth2m802dot1pEntry.setIndexNames((0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:qosEth2m802dot1pEntry.setStatus(_A)
_TagEth2Priority_Type=QosPriorityT
_TagEth2Priority_Object=MibTableColumn
tagEth2Priority=_TagEth2Priority_Object((1,3,6,1,4,1,25651,1,2,3,5,8,6,1,1,1),_TagEth2Priority_Type())
tagEth2Priority.setMaxAccess(_B)
if mibBuilder.loadTexts:tagEth2Priority.setStatus(_A)
_TagEth2Status_Type=EnableStatusT
_TagEth2Status_Object=MibTableColumn
tagEth2Status=_TagEth2Status_Object((1,3,6,1,4,1,25651,1,2,3,5,8,6,1,1,2),_TagEth2Status_Type())
tagEth2Status.setMaxAccess(_B)
if mibBuilder.loadTexts:tagEth2Status.setStatus(_A)
_QosEth2PortList_Object=MibTable
qosEth2PortList=_QosEth2PortList_Object((1,3,6,1,4,1,25651,1,2,3,5,8,6,2))
if mibBuilder.loadTexts:qosEth2PortList.setStatus(_A)
_QosEth2PortEntry_Object=MibTableRow
qosEth2PortEntry=_QosEth2PortEntry_Object((1,3,6,1,4,1,25651,1,2,3,5,8,6,2,1))
qosEth2PortEntry.setIndexNames((0,_C,_P),(0,_C,_Q))
if mibBuilder.loadTexts:qosEth2PortEntry.setStatus(_A)
_PortEth2Priority_Type=QosPriorityT
_PortEth2Priority_Object=MibTableColumn
portEth2Priority=_PortEth2Priority_Object((1,3,6,1,4,1,25651,1,2,3,5,8,6,2,1,1),_PortEth2Priority_Type())
portEth2Priority.setMaxAccess(_B)
if mibBuilder.loadTexts:portEth2Priority.setStatus(_A)
_PortEth2Status_Type=EnableStatusT
_PortEth2Status_Object=MibTableColumn
portEth2Status=_PortEth2Status_Object((1,3,6,1,4,1,25651,1,2,3,5,8,6,2,1,2),_PortEth2Status_Type())
portEth2Status.setMaxAccess(_B)
if mibBuilder.loadTexts:portEth2Status.setStatus(_A)
_QosScheduler_ObjectIdentity=ObjectIdentity
qosScheduler=_QosScheduler_ObjectIdentity((1,3,6,1,4,1,25651,1,2,3,5,8,7))
if mibBuilder.loadTexts:qosScheduler.setStatus(_A)
_QosScheduleMode_Type=QosScheduleModeT
_QosScheduleMode_Object=MibScalar
qosScheduleMode=_QosScheduleMode_Object((1,3,6,1,4,1,25651,1,2,3,5,8,7,1),_QosScheduleMode_Type())
qosScheduleMode.setMaxAccess(_B)
if mibBuilder.loadTexts:qosScheduleMode.setStatus(_A)
_QosCos3Weight_Type=QosCos3WeightT
_QosCos3Weight_Object=MibScalar
qosCos3Weight=_QosCos3Weight_Object((1,3,6,1,4,1,25651,1,2,3,5,8,7,2),_QosCos3Weight_Type())
qosCos3Weight.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCos3Weight.setStatus(_A)
_QosCos2Weight_Type=QosCos2WeightT
_QosCos2Weight_Object=MibScalar
qosCos2Weight=_QosCos2Weight_Object((1,3,6,1,4,1,25651,1,2,3,5,8,7,3),_QosCos2Weight_Type())
qosCos2Weight.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCos2Weight.setStatus(_A)
_QosCos1Weight_Type=QosCos1WeightT
_QosCos1Weight_Object=MibScalar
qosCos1Weight=_QosCos1Weight_Object((1,3,6,1,4,1,25651,1,2,3,5,8,7,4),_QosCos1Weight_Type())
qosCos1Weight.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCos1Weight.setStatus(_A)
_QosCos0Weight_Type=QosCos0WeightT
_QosCos0Weight_Object=MibScalar
qosCos0Weight=_QosCos0Weight_Object((1,3,6,1,4,1,25651,1,2,3,5,8,7,5),_QosCos0Weight_Type())
qosCos0Weight.setMaxAccess(_B)
if mibBuilder.loadTexts:qosCos0Weight.setStatus(_A)
_CommitQosSettings_Type=DisplayString
_CommitQosSettings_Object=MibScalar
commitQosSettings=_CommitQosSettings_Object((1,3,6,1,4,1,25651,1,2,3,5,8,1000),_CommitQosSettings_Type())
commitQosSettings.setMaxAccess(_B)
if mibBuilder.loadTexts:commitQosSettings.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'QosPriorityT':QosPriorityT,'QosModeT':QosModeT,'QosScheduleModeT':QosScheduleModeT,'QosCos3WeightT':QosCos3WeightT,'QosCos2WeightT':QosCos2WeightT,'QosCos1WeightT':QosCos1WeightT,'QosCos0WeightT':QosCos0WeightT,'advSystemConfig':advSystemConfig,'extAirG2QoS':extAirG2QoS,'qosDefaultQueue':qosDefaultQueue,'qosEth1Mode':qosEth1Mode,'qosEth2Mode':qosEth2Mode,'qosDiffServList':qosDiffServList,'qosDiffServEntry':qosDiffServEntry,_G:diffServValue,_H:diffServPriority,_I:diffServEnable,'qosPortETH1Conf':qosPortETH1Conf,'qosEth1m802dot1pList':qosEth1m802dot1pList,'qosEth1m802dot1pEntry':qosEth1m802dot1pEntry,_J:tagEth1Priority,_K:tagEth1Status,'qosEth1PortList':qosEth1PortList,'qosEth1PortEntry':qosEth1PortEntry,_L:portEth1Priority,_M:portEth1Status,'qosPortETH2Conf':qosPortETH2Conf,'qosEth2m802dot1pList':qosEth2m802dot1pList,'qosEth2m802dot1pEntry':qosEth2m802dot1pEntry,_N:tagEth2Priority,_O:tagEth2Status,'qosEth2PortList':qosEth2PortList,'qosEth2PortEntry':qosEth2PortEntry,_P:portEth2Priority,_Q:portEth2Status,'qosScheduler':qosScheduler,'qosScheduleMode':qosScheduleMode,'qosCos3Weight':qosCos3Weight,'qosCos2Weight':qosCos2Weight,'qosCos1Weight':qosCos1Weight,'qosCos0Weight':qosCos0Weight,'commitQosSettings':commitQosSettings})