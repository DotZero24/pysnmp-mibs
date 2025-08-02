_I='ibm2212GraphicPortNum'
_H='ibm2212GraphicSlotNum'
_G='not-present'
_F='unknown'
_E='ibm2212AdapSlotNum'
_D='IBM2212-MIB'
_C='read-only'
_B='Integer32'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2))
_IbmProd_ObjectIdentity=ObjectIdentity
ibmProd=_IbmProd_ObjectIdentity((1,3,6,1,4,1,2,6))
_Ibm2212_ObjectIdentity=ObjectIdentity
ibm2212=_Ibm2212_ObjectIdentity((1,3,6,1,4,1,2,6,149))
_Ibm2212admin_ObjectIdentity=ObjectIdentity
ibm2212admin=_Ibm2212admin_ObjectIdentity((1,3,6,1,4,1,2,6,149,1))
_Ibm2212adminproducts_ObjectIdentity=ObjectIdentity
ibm2212adminproducts=_Ibm2212adminproducts_ObjectIdentity((1,3,6,1,4,1,2,6,149,1,1))
_Ibm2212adminOID_ObjectIdentity=ObjectIdentity
ibm2212adminOID=_Ibm2212adminOID_ObjectIdentity((1,3,6,1,4,1,2,6,149,1,2))
_Ibm2212EnetChipSet_ObjectIdentity=ObjectIdentity
ibm2212EnetChipSet=_Ibm2212EnetChipSet_ObjectIdentity((1,3,6,1,4,1,2,6,149,1,2,1))
_EnetChipSetUnknown_ObjectIdentity=ObjectIdentity
enetChipSetUnknown=_EnetChipSetUnknown_ObjectIdentity((1,3,6,1,4,1,2,6,149,1,2,1,1))
_EnetChipSetAMD_ObjectIdentity=ObjectIdentity
enetChipSetAMD=_EnetChipSetAMD_ObjectIdentity((1,3,6,1,4,1,2,6,149,1,2,1,2))
_Ibm2212adminDebug_ObjectIdentity=ObjectIdentity
ibm2212adminDebug=_Ibm2212adminDebug_ObjectIdentity((1,3,6,1,4,1,2,6,149,1,3))
_Ibm2212system_ObjectIdentity=ObjectIdentity
ibm2212system=_Ibm2212system_ObjectIdentity((1,3,6,1,4,1,2,6,149,2))
_Ibm2212systemInfo_ObjectIdentity=ObjectIdentity
ibm2212systemInfo=_Ibm2212systemInfo_ObjectIdentity((1,3,6,1,4,1,2,6,149,2,1))
_Ibm2212cfgInfo_ObjectIdentity=ObjectIdentity
ibm2212cfgInfo=_Ibm2212cfgInfo_ObjectIdentity((1,3,6,1,4,1,2,6,149,2,2))
_Ibm2212hardware_ObjectIdentity=ObjectIdentity
ibm2212hardware=_Ibm2212hardware_ObjectIdentity((1,3,6,1,4,1,2,6,149,3))
_Ibm2212hardwareGeneral_ObjectIdentity=ObjectIdentity
ibm2212hardwareGeneral=_Ibm2212hardwareGeneral_ObjectIdentity((1,3,6,1,4,1,2,6,149,3,1))
_Ibm2212AdapTable_Object=MibTable
ibm2212AdapTable=_Ibm2212AdapTable_Object((1,3,6,1,4,1,2,6,149,3,1,1))
if mibBuilder.loadTexts:ibm2212AdapTable.setStatus(_A)
_Ibm2212AdapEntry_Object=MibTableRow
ibm2212AdapEntry=_Ibm2212AdapEntry_Object((1,3,6,1,4,1,2,6,149,3,1,1,1))
ibm2212AdapEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ibm2212AdapEntry.setStatus(_A)
class _Ibm2212AdapSlotNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_Ibm2212AdapSlotNum_Type.__name__=_B
_Ibm2212AdapSlotNum_Object=MibTableColumn
ibm2212AdapSlotNum=_Ibm2212AdapSlotNum_Object((1,3,6,1,4,1,2,6,149,3,1,1,1,1),_Ibm2212AdapSlotNum_Type())
ibm2212AdapSlotNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm2212AdapSlotNum.setStatus(_A)
class _Ibm2212AdapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_F,1),(_G,2),('eth-fast-1port',3),('token-ring-1port',4),('eth-fast-2port',5),('token-ring-2port',6),('serial-4port-shallow',7),('isdn-bri-u-2port',8),('isdn-bri-st-2port',9),('isdn-pri-t1j1-1port',10),('isdn-pri-e1-1port',11),('compression-encryption',12),('serial-4port-deep',13),('isdn-pri-t1j1-2port',14),('isdn-pri-e1-2port',15)))
_Ibm2212AdapType_Type.__name__=_B
_Ibm2212AdapType_Object=MibTableColumn
ibm2212AdapType=_Ibm2212AdapType_Object((1,3,6,1,4,1,2,6,149,3,1,1,1,2),_Ibm2212AdapType_Type())
ibm2212AdapType.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm2212AdapType.setStatus(_A)
class _Ibm2212AdapOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_F,1),(_G,2),('enable-pending',3),('enabled',4),('unknown-device',5),('hardware-error',6),('not-powered',7)))
_Ibm2212AdapOperStatus_Type.__name__=_B
_Ibm2212AdapOperStatus_Object=MibTableColumn
ibm2212AdapOperStatus=_Ibm2212AdapOperStatus_Object((1,3,6,1,4,1,2,6,149,3,1,1,1,3),_Ibm2212AdapOperStatus_Type())
ibm2212AdapOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm2212AdapOperStatus.setStatus(_A)
_Ibm2212GraphicTable_Object=MibTable
ibm2212GraphicTable=_Ibm2212GraphicTable_Object((1,3,6,1,4,1,2,6,149,3,1,2))
if mibBuilder.loadTexts:ibm2212GraphicTable.setStatus(_A)
_Ibm2212GraphicEntry_Object=MibTableRow
ibm2212GraphicEntry=_Ibm2212GraphicEntry_Object((1,3,6,1,4,1,2,6,149,3,1,2,1))
ibm2212GraphicEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:ibm2212GraphicEntry.setStatus(_A)
class _Ibm2212GraphicSlotNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Ibm2212GraphicSlotNum_Type.__name__=_B
_Ibm2212GraphicSlotNum_Object=MibTableColumn
ibm2212GraphicSlotNum=_Ibm2212GraphicSlotNum_Object((1,3,6,1,4,1,2,6,149,3,1,2,1,1),_Ibm2212GraphicSlotNum_Type())
ibm2212GraphicSlotNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm2212GraphicSlotNum.setStatus(_A)
class _Ibm2212GraphicPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Ibm2212GraphicPortNum_Type.__name__=_B
_Ibm2212GraphicPortNum_Object=MibTableColumn
ibm2212GraphicPortNum=_Ibm2212GraphicPortNum_Object((1,3,6,1,4,1,2,6,149,3,1,2,1,2),_Ibm2212GraphicPortNum_Type())
ibm2212GraphicPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm2212GraphicPortNum.setStatus(_A)
_Ibm2212GraphicifIndex_Type=Integer32
_Ibm2212GraphicifIndex_Object=MibTableColumn
ibm2212GraphicifIndex=_Ibm2212GraphicifIndex_Object((1,3,6,1,4,1,2,6,149,3,1,2,1,3),_Ibm2212GraphicifIndex_Type())
ibm2212GraphicifIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm2212GraphicifIndex.setStatus(_A)
_Ibm2212routing_ObjectIdentity=ObjectIdentity
ibm2212routing=_Ibm2212routing_ObjectIdentity((1,3,6,1,4,1,2,6,149,4))
_Ibm2212switching_ObjectIdentity=ObjectIdentity
ibm2212switching=_Ibm2212switching_ObjectIdentity((1,3,6,1,4,1,2,6,149,5))
mibBuilder.exportSymbols(_D,**{'ibm':ibm,'ibmProd':ibmProd,'ibm2212':ibm2212,'ibm2212admin':ibm2212admin,'ibm2212adminproducts':ibm2212adminproducts,'ibm2212adminOID':ibm2212adminOID,'ibm2212EnetChipSet':ibm2212EnetChipSet,'enetChipSetUnknown':enetChipSetUnknown,'enetChipSetAMD':enetChipSetAMD,'ibm2212adminDebug':ibm2212adminDebug,'ibm2212system':ibm2212system,'ibm2212systemInfo':ibm2212systemInfo,'ibm2212cfgInfo':ibm2212cfgInfo,'ibm2212hardware':ibm2212hardware,'ibm2212hardwareGeneral':ibm2212hardwareGeneral,'ibm2212AdapTable':ibm2212AdapTable,'ibm2212AdapEntry':ibm2212AdapEntry,_E:ibm2212AdapSlotNum,'ibm2212AdapType':ibm2212AdapType,'ibm2212AdapOperStatus':ibm2212AdapOperStatus,'ibm2212GraphicTable':ibm2212GraphicTable,'ibm2212GraphicEntry':ibm2212GraphicEntry,_H:ibm2212GraphicSlotNum,_I:ibm2212GraphicPortNum,'ibm2212GraphicifIndex':ibm2212GraphicifIndex,'ibm2212routing':ibm2212routing,'ibm2212switching':ibm2212switching})