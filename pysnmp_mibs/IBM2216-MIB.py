_I='ibm2216GraphicPortNum'
_H='ibm2216GraphicSlotNum'
_G='not-present'
_F='unknown'
_E='ibm2216PCIAdapSlotNum'
_D='IBM2216-MIB'
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
_Ibm2216_ObjectIdentity=ObjectIdentity
ibm2216=_Ibm2216_ObjectIdentity((1,3,6,1,4,1,2,6,131))
_Ibm2216admin_ObjectIdentity=ObjectIdentity
ibm2216admin=_Ibm2216admin_ObjectIdentity((1,3,6,1,4,1,2,6,131,1))
_Ibm2216adminproducts_ObjectIdentity=ObjectIdentity
ibm2216adminproducts=_Ibm2216adminproducts_ObjectIdentity((1,3,6,1,4,1,2,6,131,1,1))
_Ibm2216mod400_ObjectIdentity=ObjectIdentity
ibm2216mod400=_Ibm2216mod400_ObjectIdentity((1,3,6,1,4,1,2,6,131,1,1,1))
_Ibm2216adminOID_ObjectIdentity=ObjectIdentity
ibm2216adminOID=_Ibm2216adminOID_ObjectIdentity((1,3,6,1,4,1,2,6,131,1,2))
_Ibm2216EnetChipSet_ObjectIdentity=ObjectIdentity
ibm2216EnetChipSet=_Ibm2216EnetChipSet_ObjectIdentity((1,3,6,1,4,1,2,6,131,1,2,1))
_EnetChipSetToshiba_ObjectIdentity=ObjectIdentity
enetChipSetToshiba=_EnetChipSetToshiba_ObjectIdentity((1,3,6,1,4,1,2,6,131,1,2,1,1))
_EnetChipSetAMD_ObjectIdentity=ObjectIdentity
enetChipSetAMD=_EnetChipSetAMD_ObjectIdentity((1,3,6,1,4,1,2,6,131,1,2,1,2))
_Ibm2216adminDebug_ObjectIdentity=ObjectIdentity
ibm2216adminDebug=_Ibm2216adminDebug_ObjectIdentity((1,3,6,1,4,1,2,6,131,1,3))
_Ibm2216system_ObjectIdentity=ObjectIdentity
ibm2216system=_Ibm2216system_ObjectIdentity((1,3,6,1,4,1,2,6,131,2))
_Ibm2216systemInfo_ObjectIdentity=ObjectIdentity
ibm2216systemInfo=_Ibm2216systemInfo_ObjectIdentity((1,3,6,1,4,1,2,6,131,2,1))
_Ibm2216cfgInfo_ObjectIdentity=ObjectIdentity
ibm2216cfgInfo=_Ibm2216cfgInfo_ObjectIdentity((1,3,6,1,4,1,2,6,131,2,2))
_Ibm2216hardware_ObjectIdentity=ObjectIdentity
ibm2216hardware=_Ibm2216hardware_ObjectIdentity((1,3,6,1,4,1,2,6,131,3))
_Ibm2216hardwareGeneral_ObjectIdentity=ObjectIdentity
ibm2216hardwareGeneral=_Ibm2216hardwareGeneral_ObjectIdentity((1,3,6,1,4,1,2,6,131,3,1))
_Ibm2216PCIAdapTable_Object=MibTable
ibm2216PCIAdapTable=_Ibm2216PCIAdapTable_Object((1,3,6,1,4,1,2,6,131,3,1,1))
if mibBuilder.loadTexts:ibm2216PCIAdapTable.setStatus(_A)
_Ibm2216PCIAdapEntry_Object=MibTableRow
ibm2216PCIAdapEntry=_Ibm2216PCIAdapEntry_Object((1,3,6,1,4,1,2,6,131,3,1,1,1))
ibm2216PCIAdapEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ibm2216PCIAdapEntry.setStatus(_A)
class _Ibm2216PCIAdapSlotNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_Ibm2216PCIAdapSlotNum_Type.__name__=_B
_Ibm2216PCIAdapSlotNum_Object=MibTableColumn
ibm2216PCIAdapSlotNum=_Ibm2216PCIAdapSlotNum_Object((1,3,6,1,4,1,2,6,131,3,1,1,1,1),_Ibm2216PCIAdapSlotNum_Type())
ibm2216PCIAdapSlotNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm2216PCIAdapSlotNum.setStatus(_A)
class _Ibm2216PCIAdapType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)));namedValues=NamedValues(*((_F,1),(_G,2),('atm-mmf-lic294',3),('atm-mmf-lic284',4),('atm-smf-lic295',5),('atm-smf-lic293',6),('token-ring-lic280',7),('escon-lic287',8),('isdn-t1j1-lic283',9),('isdn-e1-lic292',10),('serial-rs232-lic282',11),('serial-v35-lic290',12),('serial-x21-lic291',13),('ethernet-lic281',14),('ethernet-fast-lic288',15),('serial-hssi-lic289',16),('fddi-lic286',17),('isdn-t1j1-lic297',18),('isdn-e1-lic298',19),('parallel-channel-lic299',20)))
_Ibm2216PCIAdapType_Type.__name__=_B
_Ibm2216PCIAdapType_Object=MibTableColumn
ibm2216PCIAdapType=_Ibm2216PCIAdapType_Object((1,3,6,1,4,1,2,6,131,3,1,1,1,2),_Ibm2216PCIAdapType_Type())
ibm2216PCIAdapType.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm2216PCIAdapType.setStatus(_A)
class _Ibm2216PCIAdapOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15)));namedValues=NamedValues(*((_F,1),('not-configured',2),(_G,3),('does-not-apply',4),('enable-pending',5),('enabled',6),('disable-pending',7),('disabled',8),('not-initialized',9),('unknown-device',10),('hardware-error',11),('not-powered',12),('diagnostics',13),('wrs-available',14),('mis-configured',15)))
_Ibm2216PCIAdapOperStatus_Type.__name__=_B
_Ibm2216PCIAdapOperStatus_Object=MibTableColumn
ibm2216PCIAdapOperStatus=_Ibm2216PCIAdapOperStatus_Object((1,3,6,1,4,1,2,6,131,3,1,1,1,3),_Ibm2216PCIAdapOperStatus_Type())
ibm2216PCIAdapOperStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm2216PCIAdapOperStatus.setStatus(_A)
_Ibm2216GraphicTable_Object=MibTable
ibm2216GraphicTable=_Ibm2216GraphicTable_Object((1,3,6,1,4,1,2,6,131,3,1,2))
if mibBuilder.loadTexts:ibm2216GraphicTable.setStatus(_A)
_Ibm2216GraphicEntry_Object=MibTableRow
ibm2216GraphicEntry=_Ibm2216GraphicEntry_Object((1,3,6,1,4,1,2,6,131,3,1,2,1))
ibm2216GraphicEntry.setIndexNames((0,_D,_H),(0,_D,_I))
if mibBuilder.loadTexts:ibm2216GraphicEntry.setStatus(_A)
class _Ibm2216GraphicSlotNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Ibm2216GraphicSlotNum_Type.__name__=_B
_Ibm2216GraphicSlotNum_Object=MibTableColumn
ibm2216GraphicSlotNum=_Ibm2216GraphicSlotNum_Object((1,3,6,1,4,1,2,6,131,3,1,2,1,1),_Ibm2216GraphicSlotNum_Type())
ibm2216GraphicSlotNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm2216GraphicSlotNum.setStatus(_A)
class _Ibm2216GraphicPortNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_Ibm2216GraphicPortNum_Type.__name__=_B
_Ibm2216GraphicPortNum_Object=MibTableColumn
ibm2216GraphicPortNum=_Ibm2216GraphicPortNum_Object((1,3,6,1,4,1,2,6,131,3,1,2,1,2),_Ibm2216GraphicPortNum_Type())
ibm2216GraphicPortNum.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm2216GraphicPortNum.setStatus(_A)
_Ibm2216GraphicifIndex_Type=Integer32
_Ibm2216GraphicifIndex_Object=MibTableColumn
ibm2216GraphicifIndex=_Ibm2216GraphicifIndex_Object((1,3,6,1,4,1,2,6,131,3,1,2,1,3),_Ibm2216GraphicifIndex_Type())
ibm2216GraphicifIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm2216GraphicifIndex.setStatus(_A)
_Ibm2216hardware400Specific_ObjectIdentity=ObjectIdentity
ibm2216hardware400Specific=_Ibm2216hardware400Specific_ObjectIdentity((1,3,6,1,4,1,2,6,131,3,2))
_Ibm2216routing_ObjectIdentity=ObjectIdentity
ibm2216routing=_Ibm2216routing_ObjectIdentity((1,3,6,1,4,1,2,6,131,4))
_Ibm2216switching_ObjectIdentity=ObjectIdentity
ibm2216switching=_Ibm2216switching_ObjectIdentity((1,3,6,1,4,1,2,6,131,5))
mibBuilder.exportSymbols(_D,**{'ibm':ibm,'ibmProd':ibmProd,'ibm2216':ibm2216,'ibm2216admin':ibm2216admin,'ibm2216adminproducts':ibm2216adminproducts,'ibm2216mod400':ibm2216mod400,'ibm2216adminOID':ibm2216adminOID,'ibm2216EnetChipSet':ibm2216EnetChipSet,'enetChipSetToshiba':enetChipSetToshiba,'enetChipSetAMD':enetChipSetAMD,'ibm2216adminDebug':ibm2216adminDebug,'ibm2216system':ibm2216system,'ibm2216systemInfo':ibm2216systemInfo,'ibm2216cfgInfo':ibm2216cfgInfo,'ibm2216hardware':ibm2216hardware,'ibm2216hardwareGeneral':ibm2216hardwareGeneral,'ibm2216PCIAdapTable':ibm2216PCIAdapTable,'ibm2216PCIAdapEntry':ibm2216PCIAdapEntry,_E:ibm2216PCIAdapSlotNum,'ibm2216PCIAdapType':ibm2216PCIAdapType,'ibm2216PCIAdapOperStatus':ibm2216PCIAdapOperStatus,'ibm2216GraphicTable':ibm2216GraphicTable,'ibm2216GraphicEntry':ibm2216GraphicEntry,_H:ibm2216GraphicSlotNum,_I:ibm2216GraphicPortNum,'ibm2216GraphicifIndex':ibm2216GraphicifIndex,'ibm2216hardware400Specific':ibm2216hardware400Specific,'ibm2216routing':ibm2216routing,'ibm2216switching':ibm2216switching})