_E='Integer32'
_D='adslLineNumber'
_C='QTECH-NMS-1705'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
nmsMgmt,=mibBuilder.importSymbols('QTECH-NMS-SMI','nmsMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
nms1705MIB=ModuleIdentity((1,3,6,1,4,1,34751,9,175))
_Nms1705Objects_ObjectIdentity=ObjectIdentity
nms1705Objects=_Nms1705Objects_ObjectIdentity((1,3,6,1,4,1,34751,9,175,1))
_AdslLineTable_Object=MibTable
adslLineTable=_AdslLineTable_Object((1,3,6,1,4,1,34751,9,175,1,1))
if mibBuilder.loadTexts:adslLineTable.setStatus(_A)
_AdslLineEntry_Object=MibTableRow
adslLineEntry=_AdslLineEntry_Object((1,3,6,1,4,1,34751,9,175,1,1,1))
adslLineEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adslLineEntry.setStatus(_A)
_AdslLineUser_Type=DisplayString
_AdslLineUser_Object=MibTableColumn
adslLineUser=_AdslLineUser_Object((1,3,6,1,4,1,34751,9,175,1,1,1,1),_AdslLineUser_Type())
adslLineUser.setMaxAccess(_B)
if mibBuilder.loadTexts:adslLineUser.setStatus(_A)
_AdslProductID_Type=DisplayString
_AdslProductID_Object=MibTableColumn
adslProductID=_AdslProductID_Object((1,3,6,1,4,1,34751,9,175,1,1,1,2),_AdslProductID_Type())
adslProductID.setMaxAccess(_B)
if mibBuilder.loadTexts:adslProductID.setStatus(_A)
_AdslConfigAddr_Type=IpAddress
_AdslConfigAddr_Object=MibTableColumn
adslConfigAddr=_AdslConfigAddr_Object((1,3,6,1,4,1,34751,9,175,1,1,1,3),_AdslConfigAddr_Type())
adslConfigAddr.setMaxAccess(_B)
if mibBuilder.loadTexts:adslConfigAddr.setStatus(_A)
_AdslLineNumber_Type=Integer32
_AdslLineNumber_Object=MibTableColumn
adslLineNumber=_AdslLineNumber_Object((1,3,6,1,4,1,34751,9,175,1,1,1,4),_AdslLineNumber_Type())
adslLineNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:adslLineNumber.setStatus(_A)
_AdslPeriodTable_Object=MibTable
adslPeriodTable=_AdslPeriodTable_Object((1,3,6,1,4,1,34751,9,175,1,2))
if mibBuilder.loadTexts:adslPeriodTable.setStatus(_A)
_AdslPeriodEntry_Object=MibTableRow
adslPeriodEntry=_AdslPeriodEntry_Object((1,3,6,1,4,1,34751,9,175,1,2,1))
adslPeriodEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:adslPeriodEntry.setStatus(_A)
_AdslMemLoad_Type=ObjectIdentifier
_AdslMemLoad_Object=MibTableColumn
adslMemLoad=_AdslMemLoad_Object((1,3,6,1,4,1,34751,9,175,1,2,1,1),_AdslMemLoad_Type())
adslMemLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:adslMemLoad.setStatus(_A)
_AdslCPULoad_Type=ObjectIdentifier
_AdslCPULoad_Object=MibTableColumn
adslCPULoad=_AdslCPULoad_Object((1,3,6,1,4,1,34751,9,175,1,2,1,2),_AdslCPULoad_Type())
adslCPULoad.setMaxAccess(_B)
if mibBuilder.loadTexts:adslCPULoad.setStatus(_A)
_AdslPtInCRC_Type=Counter32
_AdslPtInCRC_Object=MibTableColumn
adslPtInCRC=_AdslPtInCRC_Object((1,3,6,1,4,1,34751,9,175,1,2,1,3),_AdslPtInCRC_Type())
adslPtInCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:adslPtInCRC.setStatus(_A)
class _AdslPtStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_AdslPtStatus_Type.__name__=_E
_AdslPtStatus_Object=MibTableColumn
adslPtStatus=_AdslPtStatus_Object((1,3,6,1,4,1,34751,9,175,1,2,1,4),_AdslPtStatus_Type())
adslPtStatus.setMaxAccess('read-write')
if mibBuilder.loadTexts:adslPtStatus.setStatus('current')
_AdslPtSpeed_Type=ObjectIdentifier
_AdslPtSpeed_Object=MibTableColumn
adslPtSpeed=_AdslPtSpeed_Object((1,3,6,1,4,1,34751,9,175,1,2,1,5),_AdslPtSpeed_Type())
adslPtSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:adslPtSpeed.setStatus(_A)
_AdslPtOutPkts_Type=Counter32
_AdslPtOutPkts_Object=MibTableColumn
adslPtOutPkts=_AdslPtOutPkts_Object((1,3,6,1,4,1,34751,9,175,1,2,1,6),_AdslPtOutPkts_Type())
adslPtOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adslPtOutPkts.setStatus(_A)
_AdslPtInPkts_Type=Counter32
_AdslPtInPkts_Object=MibTableColumn
adslPtInPkts=_AdslPtInPkts_Object((1,3,6,1,4,1,34751,9,175,1,2,1,7),_AdslPtInPkts_Type())
adslPtInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:adslPtInPkts.setStatus(_A)
_AdslPtOutError_Type=ObjectIdentifier
_AdslPtOutError_Object=MibTableColumn
adslPtOutError=_AdslPtOutError_Object((1,3,6,1,4,1,34751,9,175,1,2,1,8),_AdslPtOutError_Type())
adslPtOutError.setMaxAccess(_B)
if mibBuilder.loadTexts:adslPtOutError.setStatus(_A)
_AdslPtInError_Type=ObjectIdentifier
_AdslPtInError_Object=MibTableColumn
adslPtInError=_AdslPtInError_Object((1,3,6,1,4,1,34751,9,175,1,2,1,9),_AdslPtInError_Type())
adslPtInError.setMaxAccess(_B)
if mibBuilder.loadTexts:adslPtInError.setStatus(_A)
_AdslPtOutSpeed_Type=ObjectIdentifier
_AdslPtOutSpeed_Object=MibTableColumn
adslPtOutSpeed=_AdslPtOutSpeed_Object((1,3,6,1,4,1,34751,9,175,1,2,1,10),_AdslPtOutSpeed_Type())
adslPtOutSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:adslPtOutSpeed.setStatus(_A)
_AdslPtInSpeed_Type=ObjectIdentifier
_AdslPtInSpeed_Object=MibTableColumn
adslPtInSpeed=_AdslPtInSpeed_Object((1,3,6,1,4,1,34751,9,175,1,2,1,11),_AdslPtInSpeed_Type())
adslPtInSpeed.setMaxAccess(_B)
if mibBuilder.loadTexts:adslPtInSpeed.setStatus(_A)
_AdslPtOutDrop_Type=ObjectIdentifier
_AdslPtOutDrop_Object=MibTableColumn
adslPtOutDrop=_AdslPtOutDrop_Object((1,3,6,1,4,1,34751,9,175,1,2,1,12),_AdslPtOutDrop_Type())
adslPtOutDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:adslPtOutDrop.setStatus(_A)
_AdslPtInDrop_Type=ObjectIdentifier
_AdslPtInDrop_Object=MibTableColumn
adslPtInDrop=_AdslPtInDrop_Object((1,3,6,1,4,1,34751,9,175,1,2,1,13),_AdslPtInDrop_Type())
adslPtInDrop.setMaxAccess(_B)
if mibBuilder.loadTexts:adslPtInDrop.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'nms1705MIB':nms1705MIB,'nms1705Objects':nms1705Objects,'adslLineTable':adslLineTable,'adslLineEntry':adslLineEntry,'adslLineUser':adslLineUser,'adslProductID':adslProductID,'adslConfigAddr':adslConfigAddr,_D:adslLineNumber,'adslPeriodTable':adslPeriodTable,'adslPeriodEntry':adslPeriodEntry,'adslMemLoad':adslMemLoad,'adslCPULoad':adslCPULoad,'adslPtInCRC':adslPtInCRC,'adslPtStatus':adslPtStatus,'adslPtSpeed':adslPtSpeed,'adslPtOutPkts':adslPtOutPkts,'adslPtInPkts':adslPtInPkts,'adslPtOutError':adslPtOutError,'adslPtInError':adslPtInError,'adslPtOutSpeed':adslPtOutSpeed,'adslPtInSpeed':adslPtInSpeed,'adslPtOutDrop':adslPtOutDrop,'adslPtInDrop':adslPtInDrop})