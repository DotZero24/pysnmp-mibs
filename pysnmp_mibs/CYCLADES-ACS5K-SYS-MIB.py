_F='powerOFF'
_E='powerON'
_D='noinstalled'
_C='Integer32'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cyACS5KMgmt,=mibBuilder.importSymbols('CYCLADES-ACS5K-MIB','cyACS5KMgmt')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
cyACS5KSys=ModuleIdentity((1,3,6,1,4,1,2925,8,1))
if mibBuilder.loadTexts:cyACS5KSys.setRevisions(('2011-05-24 00:00','2010-07-26 00:00'))
_CyACS5Kpname_Type=DisplayString
_CyACS5Kpname_Object=MibScalar
cyACS5Kpname=_CyACS5Kpname_Object((1,3,6,1,4,1,2925,8,1,1),_CyACS5Kpname_Type())
cyACS5Kpname.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACS5Kpname.setStatus(_A)
_CyACS5Kversion_Type=DisplayString
_CyACS5Kversion_Object=MibScalar
cyACS5Kversion=_CyACS5Kversion_Object((1,3,6,1,4,1,2925,8,1,2),_CyACS5Kversion_Type())
cyACS5Kversion.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACS5Kversion.setStatus(_A)
_CyACS5KPower_ObjectIdentity=ObjectIdentity
cyACS5KPower=_CyACS5KPower_ObjectIdentity((1,3,6,1,4,1,2925,8,1,3))
if mibBuilder.loadTexts:cyACS5KPower.setStatus(_A)
_CyACS5KPwNum_Type=Integer32
_CyACS5KPwNum_Object=MibScalar
cyACS5KPwNum=_CyACS5KPwNum_Object((1,3,6,1,4,1,2925,8,1,3,1),_CyACS5KPwNum_Type())
cyACS5KPwNum.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACS5KPwNum.setStatus(_A)
class _CyACS5KPw1_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),(_E,1),(_F,2)))
_CyACS5KPw1_Type.__name__=_C
_CyACS5KPw1_Object=MibScalar
cyACS5KPw1=_CyACS5KPw1_Object((1,3,6,1,4,1,2925,8,1,3,2),_CyACS5KPw1_Type())
cyACS5KPw1.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACS5KPw1.setStatus(_A)
class _CyACS5KPw2_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_D,0),(_E,1),(_F,2)))
_CyACS5KPw2_Type.__name__=_C
_CyACS5KPw2_Object=MibScalar
cyACS5KPw2=_CyACS5KPw2_Object((1,3,6,1,4,1,2925,8,1,3,3),_CyACS5KPw2_Type())
cyACS5KPw2.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACS5KPw2.setStatus(_A)
_CyACS5KPcmcia_ObjectIdentity=ObjectIdentity
cyACS5KPcmcia=_CyACS5KPcmcia_ObjectIdentity((1,3,6,1,4,1,2925,8,1,4))
if mibBuilder.loadTexts:cyACS5KPcmcia.setStatus(_A)
_CyACS5KNPcmcia_Type=Integer32
_CyACS5KNPcmcia_Object=MibScalar
cyACS5KNPcmcia=_CyACS5KNPcmcia_Object((1,3,6,1,4,1,2925,8,1,4,1),_CyACS5KNPcmcia_Type())
cyACS5KNPcmcia.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACS5KNPcmcia.setStatus(_A)
_CyACS5KFlashSize_Type=Integer32
_CyACS5KFlashSize_Object=MibScalar
cyACS5KFlashSize=_CyACS5KFlashSize_Object((1,3,6,1,4,1,2925,8,1,5),_CyACS5KFlashSize_Type())
cyACS5KFlashSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACS5KFlashSize.setStatus(_A)
_CyACS5KRAMSize_Type=Integer32
_CyACS5KRAMSize_Object=MibScalar
cyACS5KRAMSize=_CyACS5KRAMSize_Object((1,3,6,1,4,1,2925,8,1,6),_CyACS5KRAMSize_Type())
cyACS5KRAMSize.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACS5KRAMSize.setStatus(_A)
_CyACS5KCPUfreq_Type=Integer32
_CyACS5KCPUfreq_Object=MibScalar
cyACS5KCPUfreq=_CyACS5KCPUfreq_Object((1,3,6,1,4,1,2925,8,1,7),_CyACS5KCPUfreq_Type())
cyACS5KCPUfreq.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACS5KCPUfreq.setStatus(_A)
_CyACS5KDevId_Type=DisplayString
_CyACS5KDevId_Object=MibScalar
cyACS5KDevId=_CyACS5KDevId_Object((1,3,6,1,4,1,2925,8,1,8),_CyACS5KDevId_Type())
cyACS5KDevId.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACS5KDevId.setStatus(_A)
_CyACS5KSerialN_Type=DisplayString
_CyACS5KSerialN_Object=MibScalar
cyACS5KSerialN=_CyACS5KSerialN_Object((1,3,6,1,4,1,2925,8,1,9),_CyACS5KSerialN_Type())
cyACS5KSerialN.setMaxAccess(_B)
if mibBuilder.loadTexts:cyACS5KSerialN.setStatus(_A)
mibBuilder.exportSymbols('CYCLADES-ACS5K-SYS-MIB',**{'cyACS5KSys':cyACS5KSys,'cyACS5Kpname':cyACS5Kpname,'cyACS5Kversion':cyACS5Kversion,'cyACS5KPower':cyACS5KPower,'cyACS5KPwNum':cyACS5KPwNum,'cyACS5KPw1':cyACS5KPw1,'cyACS5KPw2':cyACS5KPw2,'cyACS5KPcmcia':cyACS5KPcmcia,'cyACS5KNPcmcia':cyACS5KNPcmcia,'cyACS5KFlashSize':cyACS5KFlashSize,'cyACS5KRAMSize':cyACS5KRAMSize,'cyACS5KCPUfreq':cyACS5KCPUfreq,'cyACS5KDevId':cyACS5KDevId,'cyACS5KSerialN':cyACS5KSerialN})