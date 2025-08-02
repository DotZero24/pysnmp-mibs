_K='tpQosDSCPPriTag'
_J='tpQos8021pPriTag'
_I='tpQosSchedulerConfigTc'
_H='ifIndex'
_G='IF-MIB'
_F='OctetString'
_E='TPLINK-QOS-MIB'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_F,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
tplinkMgmt,=mibBuilder.importSymbols('TPLINK-MIB','tplinkMgmt')
tplinkQosMIB=ModuleIdentity((1,3,6,1,4,1,11863,6,22))
if mibBuilder.loadTexts:tplinkQosMIB.setRevisions(('2012-12-13 09:30',))
_TplinkQosMIBObjects_ObjectIdentity=ObjectIdentity
tplinkQosMIBObjects=_TplinkQosMIBObjects_ObjectIdentity((1,3,6,1,4,1,11863,6,22,1))
_TplinkQosBasicConfig_ObjectIdentity=ObjectIdentity
tplinkQosBasicConfig=_TplinkQosBasicConfig_ObjectIdentity((1,3,6,1,4,1,11863,6,22,1,1))
_TpQosBasicConfigTable_Object=MibTable
tpQosBasicConfigTable=_TpQosBasicConfigTable_Object((1,3,6,1,4,1,11863,6,22,1,1,1))
if mibBuilder.loadTexts:tpQosBasicConfigTable.setStatus(_A)
_TpQosBasicConfigEntry_Object=MibTableRow
tpQosBasicConfigEntry=_TpQosBasicConfigEntry_Object((1,3,6,1,4,1,11863,6,22,1,1,1,1))
tpQosBasicConfigEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:tpQosBasicConfigEntry.setStatus(_A)
_TpQosBasicConfigPort_Type=DisplayString
_TpQosBasicConfigPort_Object=MibTableColumn
tpQosBasicConfigPort=_TpQosBasicConfigPort_Object((1,3,6,1,4,1,11863,6,22,1,1,1,1,1),_TpQosBasicConfigPort_Type())
tpQosBasicConfigPort.setMaxAccess(_D)
if mibBuilder.loadTexts:tpQosBasicConfigPort.setStatus(_A)
class _TpQosBasicConfigPri_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('cos0',0),('cos1',1),('cos2',2),('cos3',3),('cos4',4),('cos5',5),('cos6',6),('cos7',7)))
_TpQosBasicConfigPri_Type.__name__=_C
_TpQosBasicConfigPri_Object=MibTableColumn
tpQosBasicConfigPri=_TpQosBasicConfigPri_Object((1,3,6,1,4,1,11863,6,22,1,1,1,1,2),_TpQosBasicConfigPri_Type())
tpQosBasicConfigPri.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQosBasicConfigPri.setStatus(_A)
class _TpQosBasicConfigTrust_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('untrust',0),('trust-8021p',1),('trust-DSCP',2)))
_TpQosBasicConfigTrust_Type.__name__=_C
_TpQosBasicConfigTrust_Object=MibTableColumn
tpQosBasicConfigTrust=_TpQosBasicConfigTrust_Object((1,3,6,1,4,1,11863,6,22,1,1,1,1,3),_TpQosBasicConfigTrust_Type())
tpQosBasicConfigTrust.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQosBasicConfigTrust.setStatus(_A)
class _TpQosBasicConfigLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_TpQosBasicConfigLag_Type.__name__=_F
_TpQosBasicConfigLag_Object=MibTableColumn
tpQosBasicConfigLag=_TpQosBasicConfigLag_Object((1,3,6,1,4,1,11863,6,22,1,1,1,1,4),_TpQosBasicConfigLag_Type())
tpQosBasicConfigLag.setMaxAccess(_D)
if mibBuilder.loadTexts:tpQosBasicConfigLag.setStatus(_A)
_TplinkQosScheduler_ObjectIdentity=ObjectIdentity
tplinkQosScheduler=_TplinkQosScheduler_ObjectIdentity((1,3,6,1,4,1,11863,6,22,1,2))
_TpQosSchedulerPort_Type=OctetString
_TpQosSchedulerPort_Object=MibScalar
tpQosSchedulerPort=_TpQosSchedulerPort_Object((1,3,6,1,4,1,11863,6,22,1,2,1),_TpQosSchedulerPort_Type())
tpQosSchedulerPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQosSchedulerPort.setStatus(_A)
_TpQosSchedulerTable_Object=MibTable
tpQosSchedulerTable=_TpQosSchedulerTable_Object((1,3,6,1,4,1,11863,6,22,1,2,2))
if mibBuilder.loadTexts:tpQosSchedulerTable.setStatus(_A)
_TpQosSchedulerEntry_Object=MibTableRow
tpQosSchedulerEntry=_TpQosSchedulerEntry_Object((1,3,6,1,4,1,11863,6,22,1,2,2,1))
tpQosSchedulerEntry.setIndexNames((0,_E,_I))
if mibBuilder.loadTexts:tpQosSchedulerEntry.setStatus(_A)
class _TpQosSchedulerConfigTc_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('tc0',0),('tc1',1),('tc2',2),('tc3',3),('tc4',4),('tc5',5),('tc6',6),('tc7',7)))
_TpQosSchedulerConfigTc_Type.__name__=_C
_TpQosSchedulerConfigTc_Object=MibTableColumn
tpQosSchedulerConfigTc=_TpQosSchedulerConfigTc_Object((1,3,6,1,4,1,11863,6,22,1,2,2,1,1),_TpQosSchedulerConfigTc_Type())
tpQosSchedulerConfigTc.setMaxAccess(_D)
if mibBuilder.loadTexts:tpQosSchedulerConfigTc.setStatus(_A)
class _TpQosSchedulerConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('strict',0),('weighted',1)))
_TpQosSchedulerConfigMode_Type.__name__=_C
_TpQosSchedulerConfigMode_Object=MibTableColumn
tpQosSchedulerConfigMode=_TpQosSchedulerConfigMode_Object((1,3,6,1,4,1,11863,6,22,1,2,2,1,2),_TpQosSchedulerConfigMode_Type())
tpQosSchedulerConfigMode.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQosSchedulerConfigMode.setStatus(_A)
_TpQosSchedulerConfigWeight_Type=Integer32
_TpQosSchedulerConfigWeight_Object=MibTableColumn
tpQosSchedulerConfigWeight=_TpQosSchedulerConfigWeight_Object((1,3,6,1,4,1,11863,6,22,1,2,2,1,3),_TpQosSchedulerConfigWeight_Type())
tpQosSchedulerConfigWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQosSchedulerConfigWeight.setStatus(_A)
_TpQosSchedulerConfigMinBandwidth_Type=Integer32
_TpQosSchedulerConfigMinBandwidth_Object=MibTableColumn
tpQosSchedulerConfigMinBandwidth=_TpQosSchedulerConfigMinBandwidth_Object((1,3,6,1,4,1,11863,6,22,1,2,2,1,4),_TpQosSchedulerConfigMinBandwidth_Type())
tpQosSchedulerConfigMinBandwidth.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQosSchedulerConfigMinBandwidth.setStatus(_A)
class _TpQosSchedulerConfigManagementType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(0));namedValues=NamedValues(('taildrop',0))
_TpQosSchedulerConfigManagementType_Type.__name__=_C
_TpQosSchedulerConfigManagementType_Object=MibTableColumn
tpQosSchedulerConfigManagementType=_TpQosSchedulerConfigManagementType_Object((1,3,6,1,4,1,11863,6,22,1,2,2,1,5),_TpQosSchedulerConfigManagementType_Type())
tpQosSchedulerConfigManagementType.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQosSchedulerConfigManagementType.setStatus(_A)
_TplinkQos8021p_ObjectIdentity=ObjectIdentity
tplinkQos8021p=_TplinkQos8021p_ObjectIdentity((1,3,6,1,4,1,11863,6,22,1,3))
_TpQos8021pTable_Object=MibTable
tpQos8021pTable=_TpQos8021pTable_Object((1,3,6,1,4,1,11863,6,22,1,3,1))
if mibBuilder.loadTexts:tpQos8021pTable.setStatus(_A)
_TpQos8021pEntry_Object=MibTableRow
tpQos8021pEntry=_TpQos8021pEntry_Object((1,3,6,1,4,1,11863,6,22,1,3,1,1))
tpQos8021pEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:tpQos8021pEntry.setStatus(_A)
_TpQos8021pPriTag_Type=Integer32
_TpQos8021pPriTag_Object=MibTableColumn
tpQos8021pPriTag=_TpQos8021pPriTag_Object((1,3,6,1,4,1,11863,6,22,1,3,1,1,1),_TpQos8021pPriTag_Type())
tpQos8021pPriTag.setMaxAccess(_D)
if mibBuilder.loadTexts:tpQos8021pPriTag.setStatus(_A)
class _TpQos8021pPriLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('tc0',0),('tc1',1),('tc2',2),('tc3',3),('tc4',4),('tc5',5),('tc6',6),('tc7',7)))
_TpQos8021pPriLevel_Type.__name__=_C
_TpQos8021pPriLevel_Object=MibTableColumn
tpQos8021pPriLevel=_TpQos8021pPriLevel_Object((1,3,6,1,4,1,11863,6,22,1,3,1,1,2),_TpQos8021pPriLevel_Type())
tpQos8021pPriLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQos8021pPriLevel.setStatus(_A)
_TplinkQos8021pRemap_ObjectIdentity=ObjectIdentity
tplinkQos8021pRemap=_TplinkQos8021pRemap_ObjectIdentity((1,3,6,1,4,1,11863,6,22,1,4))
_TpQos8021pRemapTable_Object=MibTable
tpQos8021pRemapTable=_TpQos8021pRemapTable_Object((1,3,6,1,4,1,11863,6,22,1,4,1))
if mibBuilder.loadTexts:tpQos8021pRemapTable.setStatus(_A)
_TpQos8021pRemapEntry_Object=MibTableRow
tpQos8021pRemapEntry=_TpQos8021pRemapEntry_Object((1,3,6,1,4,1,11863,6,22,1,4,1,1))
tpQos8021pRemapEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:tpQos8021pRemapEntry.setStatus(_A)
_TpQos8021pPort_Type=DisplayString
_TpQos8021pPort_Object=MibTableColumn
tpQos8021pPort=_TpQos8021pPort_Object((1,3,6,1,4,1,11863,6,22,1,4,1,1,1),_TpQos8021pPort_Type())
tpQos8021pPort.setMaxAccess(_D)
if mibBuilder.loadTexts:tpQos8021pPort.setStatus(_A)
_TpQos8021pPriTag0_Type=Integer32
_TpQos8021pPriTag0_Object=MibTableColumn
tpQos8021pPriTag0=_TpQos8021pPriTag0_Object((1,3,6,1,4,1,11863,6,22,1,4,1,1,2),_TpQos8021pPriTag0_Type())
tpQos8021pPriTag0.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQos8021pPriTag0.setStatus(_A)
_TpQos8021pPriTag1_Type=Integer32
_TpQos8021pPriTag1_Object=MibTableColumn
tpQos8021pPriTag1=_TpQos8021pPriTag1_Object((1,3,6,1,4,1,11863,6,22,1,4,1,1,3),_TpQos8021pPriTag1_Type())
tpQos8021pPriTag1.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQos8021pPriTag1.setStatus(_A)
_TpQos8021pPriTag2_Type=Integer32
_TpQos8021pPriTag2_Object=MibTableColumn
tpQos8021pPriTag2=_TpQos8021pPriTag2_Object((1,3,6,1,4,1,11863,6,22,1,4,1,1,4),_TpQos8021pPriTag2_Type())
tpQos8021pPriTag2.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQos8021pPriTag2.setStatus(_A)
_TpQos8021pPriTag3_Type=Integer32
_TpQos8021pPriTag3_Object=MibTableColumn
tpQos8021pPriTag3=_TpQos8021pPriTag3_Object((1,3,6,1,4,1,11863,6,22,1,4,1,1,5),_TpQos8021pPriTag3_Type())
tpQos8021pPriTag3.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQos8021pPriTag3.setStatus(_A)
_TpQos8021pPriTag4_Type=Integer32
_TpQos8021pPriTag4_Object=MibTableColumn
tpQos8021pPriTag4=_TpQos8021pPriTag4_Object((1,3,6,1,4,1,11863,6,22,1,4,1,1,6),_TpQos8021pPriTag4_Type())
tpQos8021pPriTag4.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQos8021pPriTag4.setStatus(_A)
_TpQos8021pPriTag5_Type=Integer32
_TpQos8021pPriTag5_Object=MibTableColumn
tpQos8021pPriTag5=_TpQos8021pPriTag5_Object((1,3,6,1,4,1,11863,6,22,1,4,1,1,7),_TpQos8021pPriTag5_Type())
tpQos8021pPriTag5.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQos8021pPriTag5.setStatus(_A)
_TpQos8021pPriTag6_Type=Integer32
_TpQos8021pPriTag6_Object=MibTableColumn
tpQos8021pPriTag6=_TpQos8021pPriTag6_Object((1,3,6,1,4,1,11863,6,22,1,4,1,1,8),_TpQos8021pPriTag6_Type())
tpQos8021pPriTag6.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQos8021pPriTag6.setStatus(_A)
_TpQos8021pPriTag7_Type=Integer32
_TpQos8021pPriTag7_Object=MibTableColumn
tpQos8021pPriTag7=_TpQos8021pPriTag7_Object((1,3,6,1,4,1,11863,6,22,1,4,1,1,9),_TpQos8021pPriTag7_Type())
tpQos8021pPriTag7.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQos8021pPriTag7.setStatus(_A)
class _TpQos8021pPriLag_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,255))
_TpQos8021pPriLag_Type.__name__=_F
_TpQos8021pPriLag_Object=MibTableColumn
tpQos8021pPriLag=_TpQos8021pPriLag_Object((1,3,6,1,4,1,11863,6,22,1,4,1,1,10),_TpQos8021pPriLag_Type())
tpQos8021pPriLag.setMaxAccess(_D)
if mibBuilder.loadTexts:tpQos8021pPriLag.setStatus(_A)
_TplinkQosDSCP_ObjectIdentity=ObjectIdentity
tplinkQosDSCP=_TplinkQosDSCP_ObjectIdentity((1,3,6,1,4,1,11863,6,22,1,5))
_TpQosDSCPPort_Type=OctetString
_TpQosDSCPPort_Object=MibScalar
tpQosDSCPPort=_TpQosDSCPPort_Object((1,3,6,1,4,1,11863,6,22,1,5,1),_TpQosDSCPPort_Type())
tpQosDSCPPort.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQosDSCPPort.setStatus(_A)
_TpQosDSCPTable_Object=MibTable
tpQosDSCPTable=_TpQosDSCPTable_Object((1,3,6,1,4,1,11863,6,22,1,5,2))
if mibBuilder.loadTexts:tpQosDSCPTable.setStatus(_A)
_TpQosDSCPEntry_Object=MibTableRow
tpQosDSCPEntry=_TpQosDSCPEntry_Object((1,3,6,1,4,1,11863,6,22,1,5,2,1))
tpQosDSCPEntry.setIndexNames((0,_E,_K))
if mibBuilder.loadTexts:tpQosDSCPEntry.setStatus(_A)
_TpQosDSCPPriTag_Type=Integer32
_TpQosDSCPPriTag_Object=MibTableColumn
tpQosDSCPPriTag=_TpQosDSCPPriTag_Object((1,3,6,1,4,1,11863,6,22,1,5,2,1,1),_TpQosDSCPPriTag_Type())
tpQosDSCPPriTag.setMaxAccess(_D)
if mibBuilder.loadTexts:tpQosDSCPPriTag.setStatus(_A)
class _TpQosDSCPPriLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*(('cos0',0),('cos1',1),('cos2',2),('cos3',3),('cos4',4),('cos5',5),('cos6',6),('cos7',7)))
_TpQosDSCPPriLevel_Type.__name__=_C
_TpQosDSCPPriLevel_Object=MibTableColumn
tpQosDSCPPriLevel=_TpQosDSCPPriLevel_Object((1,3,6,1,4,1,11863,6,22,1,5,2,1,2),_TpQosDSCPPriLevel_Type())
tpQosDSCPPriLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQosDSCPPriLevel.setStatus(_A)
_TpQosDSCPPriRemap_Type=Integer32
_TpQosDSCPPriRemap_Object=MibTableColumn
tpQosDSCPPriRemap=_TpQosDSCPPriRemap_Object((1,3,6,1,4,1,11863,6,22,1,5,2,1,3),_TpQosDSCPPriRemap_Type())
tpQosDSCPPriRemap.setMaxAccess(_B)
if mibBuilder.loadTexts:tpQosDSCPPriRemap.setStatus(_A)
_TplinkQosNotifications_ObjectIdentity=ObjectIdentity
tplinkQosNotifications=_TplinkQosNotifications_ObjectIdentity((1,3,6,1,4,1,11863,6,22,2))
mibBuilder.exportSymbols(_E,**{'tplinkQosMIB':tplinkQosMIB,'tplinkQosMIBObjects':tplinkQosMIBObjects,'tplinkQosBasicConfig':tplinkQosBasicConfig,'tpQosBasicConfigTable':tpQosBasicConfigTable,'tpQosBasicConfigEntry':tpQosBasicConfigEntry,'tpQosBasicConfigPort':tpQosBasicConfigPort,'tpQosBasicConfigPri':tpQosBasicConfigPri,'tpQosBasicConfigTrust':tpQosBasicConfigTrust,'tpQosBasicConfigLag':tpQosBasicConfigLag,'tplinkQosScheduler':tplinkQosScheduler,'tpQosSchedulerPort':tpQosSchedulerPort,'tpQosSchedulerTable':tpQosSchedulerTable,'tpQosSchedulerEntry':tpQosSchedulerEntry,_I:tpQosSchedulerConfigTc,'tpQosSchedulerConfigMode':tpQosSchedulerConfigMode,'tpQosSchedulerConfigWeight':tpQosSchedulerConfigWeight,'tpQosSchedulerConfigMinBandwidth':tpQosSchedulerConfigMinBandwidth,'tpQosSchedulerConfigManagementType':tpQosSchedulerConfigManagementType,'tplinkQos8021p':tplinkQos8021p,'tpQos8021pTable':tpQos8021pTable,'tpQos8021pEntry':tpQos8021pEntry,_J:tpQos8021pPriTag,'tpQos8021pPriLevel':tpQos8021pPriLevel,'tplinkQos8021pRemap':tplinkQos8021pRemap,'tpQos8021pRemapTable':tpQos8021pRemapTable,'tpQos8021pRemapEntry':tpQos8021pRemapEntry,'tpQos8021pPort':tpQos8021pPort,'tpQos8021pPriTag0':tpQos8021pPriTag0,'tpQos8021pPriTag1':tpQos8021pPriTag1,'tpQos8021pPriTag2':tpQos8021pPriTag2,'tpQos8021pPriTag3':tpQos8021pPriTag3,'tpQos8021pPriTag4':tpQos8021pPriTag4,'tpQos8021pPriTag5':tpQos8021pPriTag5,'tpQos8021pPriTag6':tpQos8021pPriTag6,'tpQos8021pPriTag7':tpQos8021pPriTag7,'tpQos8021pPriLag':tpQos8021pPriLag,'tplinkQosDSCP':tplinkQosDSCP,'tpQosDSCPPort':tpQosDSCPPort,'tpQosDSCPTable':tpQosDSCPTable,'tpQosDSCPEntry':tpQosDSCPEntry,_K:tpQosDSCPPriTag,'tpQosDSCPPriLevel':tpQosDSCPPriLevel,'tpQosDSCPPriRemap':tpQosDSCPPriRemap,'tplinkQosNotifications':tplinkQosNotifications})