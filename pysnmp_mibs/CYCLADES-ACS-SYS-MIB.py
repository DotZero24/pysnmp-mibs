_K='cyCardStatusIndex'
_J='cyCardConfIndex'
_I='cyCardIdentIndex'
_H='powerOFF'
_G='powerON'
_F='noinstalled'
_E='2005-08-29 00:00'
_D='CYCLADES-ACS-SYS-MIB'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cyACSMgmt,=mibBuilder.importSymbols('CYCLADES-ACS-MIB','cyACSMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cyACSSys=ModuleIdentity((1,3,6,1,4,1,2925,4,1))
if mibBuilder.loadTexts:cyACSSys.setRevisions((_E,_E,'2003-06-30 00:00','2002-10-10 00:00','2002-09-20 00:00'))
_CyACSpname_Type=DisplayString
_CyACSpname_Object=MibScalar
cyACSpname=_CyACSpname_Object((1,3,6,1,4,1,2925,4,1,1),_CyACSpname_Type())
cyACSpname.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACSpname.setStatus(_A)
_CyACSversion_Type=DisplayString
_CyACSversion_Object=MibScalar
cyACSversion=_CyACSversion_Object((1,3,6,1,4,1,2925,4,1,2),_CyACSversion_Type())
cyACSversion.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACSversion.setStatus(_A)
_CyACSPower_ObjectIdentity=ObjectIdentity
cyACSPower=_CyACSPower_ObjectIdentity((1,3,6,1,4,1,2925,4,1,3))
if mibBuilder.loadTexts:cyACSPower.setStatus(_A)
_CyACSPwNum_Type=Integer32
_CyACSPwNum_Object=MibScalar
cyACSPwNum=_CyACSPwNum_Object((1,3,6,1,4,1,2925,4,1,3,1),_CyACSPwNum_Type())
cyACSPwNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACSPwNum.setStatus(_A)
class _CyACSPw1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2)))
_CyACSPw1_Type.__name__=_C
_CyACSPw1_Object=MibScalar
cyACSPw1=_CyACSPw1_Object((1,3,6,1,4,1,2925,4,1,3,2),_CyACSPw1_Type())
cyACSPw1.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACSPw1.setStatus(_A)
class _CyACSPw2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2)))
_CyACSPw2_Type.__name__=_C
_CyACSPw2_Object=MibScalar
cyACSPw2=_CyACSPw2_Object((1,3,6,1,4,1,2925,4,1,3,3),_CyACSPw2_Type())
cyACSPw2.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACSPw2.setStatus(_A)
_CyACSPcmcia_ObjectIdentity=ObjectIdentity
cyACSPcmcia=_CyACSPcmcia_ObjectIdentity((1,3,6,1,4,1,2925,4,1,4))
if mibBuilder.loadTexts:cyACSPcmcia.setStatus(_A)
_CyACSNPcmcia_Type=Integer32
_CyACSNPcmcia_Object=MibScalar
cyACSNPcmcia=_CyACSNPcmcia_Object((1,3,6,1,4,1,2925,4,1,4,1),_CyACSNPcmcia_Type())
cyACSNPcmcia.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACSNPcmcia.setStatus(_A)
_CyCardIdentTable_Object=MibTable
cyCardIdentTable=_CyCardIdentTable_Object((1,3,6,1,4,1,2925,4,1,4,2))
if mibBuilder.loadTexts:cyCardIdentTable.setStatus(_A)
_CyCardIdentEntry_Object=MibTableRow
cyCardIdentEntry=_CyCardIdentEntry_Object((1,3,6,1,4,1,2925,4,1,4,2,1))
cyCardIdentEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:cyCardIdentEntry.setStatus(_A)
class _CyCardIdentIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_CyCardIdentIndex_Type.__name__=_C
_CyCardIdentIndex_Object=MibTableColumn
cyCardIdentIndex=_CyCardIdentIndex_Object((1,3,6,1,4,1,2925,4,1,4,2,1,1),_CyCardIdentIndex_Type())
cyCardIdentIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cyCardIdentIndex.setStatus(_A)
_CyCardIdentProd_Type=DisplayString
_CyCardIdentProd_Object=MibTableColumn
cyCardIdentProd=_CyCardIdentProd_Object((1,3,6,1,4,1,2925,4,1,4,2,1,2),_CyCardIdentProd_Type())
cyCardIdentProd.setMaxAccess(_B)
if mibBuilder.loadTexts:cyCardIdentProd.setStatus(_A)
_CyCardIdentMan_Type=DisplayString
_CyCardIdentMan_Object=MibTableColumn
cyCardIdentMan=_CyCardIdentMan_Object((1,3,6,1,4,1,2925,4,1,4,2,1,3),_CyCardIdentMan_Type())
cyCardIdentMan.setMaxAccess(_B)
if mibBuilder.loadTexts:cyCardIdentMan.setStatus(_A)
_CyCardIdentFunc_Type=DisplayString
_CyCardIdentFunc_Object=MibTableColumn
cyCardIdentFunc=_CyCardIdentFunc_Object((1,3,6,1,4,1,2925,4,1,4,2,1,4),_CyCardIdentFunc_Type())
cyCardIdentFunc.setMaxAccess(_B)
if mibBuilder.loadTexts:cyCardIdentFunc.setStatus(_A)
_CyCardIdentPCI_Type=DisplayString
_CyCardIdentPCI_Object=MibTableColumn
cyCardIdentPCI=_CyCardIdentPCI_Object((1,3,6,1,4,1,2925,4,1,4,2,1,5),_CyCardIdentPCI_Type())
cyCardIdentPCI.setMaxAccess(_B)
if mibBuilder.loadTexts:cyCardIdentPCI.setStatus(_A)
_CyCardConfTable_Object=MibTable
cyCardConfTable=_CyCardConfTable_Object((1,3,6,1,4,1,2925,4,1,4,3))
if mibBuilder.loadTexts:cyCardConfTable.setStatus(_A)
_CyCardConfEntry_Object=MibTableRow
cyCardConfEntry=_CyCardConfEntry_Object((1,3,6,1,4,1,2925,4,1,4,3,1))
cyCardConfEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:cyCardConfEntry.setStatus(_A)
class _CyCardConfIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_CyCardConfIndex_Type.__name__=_C
_CyCardConfIndex_Object=MibTableColumn
cyCardConfIndex=_CyCardConfIndex_Object((1,3,6,1,4,1,2925,4,1,4,3,1,1),_CyCardConfIndex_Type())
cyCardConfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cyCardConfIndex.setStatus(_A)
_CyCardConfPower_Type=DisplayString
_CyCardConfPower_Object=MibTableColumn
cyCardConfPower=_CyCardConfPower_Object((1,3,6,1,4,1,2925,4,1,4,3,1,2),_CyCardConfPower_Type())
cyCardConfPower.setMaxAccess(_B)
if mibBuilder.loadTexts:cyCardConfPower.setStatus(_A)
_CyCardConfType_Type=DisplayString
_CyCardConfType_Object=MibTableColumn
cyCardConfType=_CyCardConfType_Object((1,3,6,1,4,1,2925,4,1,4,3,1,3),_CyCardConfType_Type())
cyCardConfType.setMaxAccess(_B)
if mibBuilder.loadTexts:cyCardConfType.setStatus(_A)
_CyCardConfInter_Type=DisplayString
_CyCardConfInter_Object=MibTableColumn
cyCardConfInter=_CyCardConfInter_Object((1,3,6,1,4,1,2925,4,1,4,3,1,4),_CyCardConfInter_Type())
cyCardConfInter.setMaxAccess(_B)
if mibBuilder.loadTexts:cyCardConfInter.setStatus(_A)
_CyCardConfFunc_Type=DisplayString
_CyCardConfFunc_Object=MibTableColumn
cyCardConfFunc=_CyCardConfFunc_Object((1,3,6,1,4,1,2925,4,1,4,3,1,5),_CyCardConfFunc_Type())
cyCardConfFunc.setMaxAccess(_B)
if mibBuilder.loadTexts:cyCardConfFunc.setStatus(_A)
_CyCardConfCardv_Type=DisplayString
_CyCardConfCardv_Object=MibTableColumn
cyCardConfCardv=_CyCardConfCardv_Object((1,3,6,1,4,1,2925,4,1,4,3,1,6),_CyCardConfCardv_Type())
cyCardConfCardv.setMaxAccess(_B)
if mibBuilder.loadTexts:cyCardConfCardv.setStatus(_A)
_CyCardConfPort1_Type=DisplayString
_CyCardConfPort1_Object=MibTableColumn
cyCardConfPort1=_CyCardConfPort1_Object((1,3,6,1,4,1,2925,4,1,4,3,1,7),_CyCardConfPort1_Type())
cyCardConfPort1.setMaxAccess(_B)
if mibBuilder.loadTexts:cyCardConfPort1.setStatus(_A)
_CyCardConfPort2_Type=DisplayString
_CyCardConfPort2_Object=MibTableColumn
cyCardConfPort2=_CyCardConfPort2_Object((1,3,6,1,4,1,2925,4,1,4,3,1,8),_CyCardConfPort2_Type())
cyCardConfPort2.setMaxAccess(_B)
if mibBuilder.loadTexts:cyCardConfPort2.setStatus(_A)
_CyCardStatusTable_Object=MibTable
cyCardStatusTable=_CyCardStatusTable_Object((1,3,6,1,4,1,2925,4,1,4,4))
if mibBuilder.loadTexts:cyCardStatusTable.setStatus(_A)
_CyCardStatusEntry_Object=MibTableRow
cyCardStatusEntry=_CyCardStatusEntry_Object((1,3,6,1,4,1,2925,4,1,4,4,1))
cyCardStatusEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:cyCardStatusEntry.setStatus(_A)
class _CyCardStatusIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_CyCardStatusIndex_Type.__name__=_C
_CyCardStatusIndex_Object=MibTableColumn
cyCardStatusIndex=_CyCardStatusIndex_Object((1,3,6,1,4,1,2925,4,1,4,4,1,1),_CyCardStatusIndex_Type())
cyCardStatusIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:cyCardStatusIndex.setStatus(_A)
_CyCardStatusCard_Type=DisplayString
_CyCardStatusCard_Object=MibTableColumn
cyCardStatusCard=_CyCardStatusCard_Object((1,3,6,1,4,1,2925,4,1,4,4,1,2),_CyCardStatusCard_Type())
cyCardStatusCard.setMaxAccess(_B)
if mibBuilder.loadTexts:cyCardStatusCard.setStatus(_A)
_CyCardStatusFunc_Type=DisplayString
_CyCardStatusFunc_Object=MibTableColumn
cyCardStatusFunc=_CyCardStatusFunc_Object((1,3,6,1,4,1,2925,4,1,4,4,1,3),_CyCardStatusFunc_Type())
cyCardStatusFunc.setMaxAccess(_B)
if mibBuilder.loadTexts:cyCardStatusFunc.setStatus(_A)
_CyACSFlashSize_Type=Integer32
_CyACSFlashSize_Object=MibScalar
cyACSFlashSize=_CyACSFlashSize_Object((1,3,6,1,4,1,2925,4,1,5),_CyACSFlashSize_Type())
cyACSFlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACSFlashSize.setStatus(_A)
_CyACSRAMSize_Type=Integer32
_CyACSRAMSize_Object=MibScalar
cyACSRAMSize=_CyACSRAMSize_Object((1,3,6,1,4,1,2925,4,1,6),_CyACSRAMSize_Type())
cyACSRAMSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACSRAMSize.setStatus(_A)
_CyACSCPUfreq_Type=Integer32
_CyACSCPUfreq_Object=MibScalar
cyACSCPUfreq=_CyACSCPUfreq_Object((1,3,6,1,4,1,2925,4,1,7),_CyACSCPUfreq_Type())
cyACSCPUfreq.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACSCPUfreq.setStatus(_A)
_CyACSDevId_Type=DisplayString
_CyACSDevId_Object=MibScalar
cyACSDevId=_CyACSDevId_Object((1,3,6,1,4,1,2925,4,1,8),_CyACSDevId_Type())
cyACSDevId.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACSDevId.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'cyACSSys':cyACSSys,'cyACSpname':cyACSpname,'cyACSversion':cyACSversion,'cyACSPower':cyACSPower,'cyACSPwNum':cyACSPwNum,'cyACSPw1':cyACSPw1,'cyACSPw2':cyACSPw2,'cyACSPcmcia':cyACSPcmcia,'cyACSNPcmcia':cyACSNPcmcia,'cyCardIdentTable':cyCardIdentTable,'cyCardIdentEntry':cyCardIdentEntry,_I:cyCardIdentIndex,'cyCardIdentProd':cyCardIdentProd,'cyCardIdentMan':cyCardIdentMan,'cyCardIdentFunc':cyCardIdentFunc,'cyCardIdentPCI':cyCardIdentPCI,'cyCardConfTable':cyCardConfTable,'cyCardConfEntry':cyCardConfEntry,_J:cyCardConfIndex,'cyCardConfPower':cyCardConfPower,'cyCardConfType':cyCardConfType,'cyCardConfInter':cyCardConfInter,'cyCardConfFunc':cyCardConfFunc,'cyCardConfCardv':cyCardConfCardv,'cyCardConfPort1':cyCardConfPort1,'cyCardConfPort2':cyCardConfPort2,'cyCardStatusTable':cyCardStatusTable,'cyCardStatusEntry':cyCardStatusEntry,_K:cyCardStatusIndex,'cyCardStatusCard':cyCardStatusCard,'cyCardStatusFunc':cyCardStatusFunc,'cyACSFlashSize':cyACSFlashSize,'cyACSRAMSize':cyACSRAMSize,'cyACSCPUfreq':cyACSCPUfreq,'cyACSDevId':cyACSDevId})