_p='aluLicenseManagerInfoGroup'
_o='aluLicenseManagerDemoInfoGroup'
_n='aluLicenseManagerRemoveInfoGroup'
_m='aluLicenseManagerFileInfoGroup'
_l='aluLicenseManagerNotificationsGroup'
_k='aluLicenseManagerLicenseInfoGroup'
_j='aluLicenseManagerConfigGroup'
_i='aluLicenseManagerLicenseExpiry'
_h='aluLicenseManagerLicenseExpired'
_g='aluLicensedInfoSlot'
_f='aluLicenseInfoFeature'
_e='aluLicenseInfoType'
_d='aluLicenseDemoSlotID'
_c='aluLicenseDemoFeatureID'
_b='aluLicenseRemoveSlotID'
_a='aluLicenseRemoveFeatureID'
_Z='aluLicensedFileLocal'
_Y='aluLicensedFileApplication'
_X='aluSwitchMacAddress'
_W='aluLicenseType'
_V='aluLicensedFileName'
_U='aluLicenseManagerApplyLicense'
_T='aluLicensedInfoApplication'
_S='aluLicenseInfoSlotId'
_R='aluLicenseDemoIndex'
_Q='tenGig'
_P='oneGig'
_O='aluLicenseRemoveIndex'
_N='aluLicenseFileIndex'
_M='permanent'
_L='aluLicenseId'
_K='aluLicenseInfoTimeRemaining'
_J='aluLicenseTimeRemaining'
_I='aluLicensedApplication'
_H='Unsigned32'
_G='not-accessible'
_F='DisplayString'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='ALCATEL-IND1-LICENSE-MANAGER-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
softentIND1LicenseManager,=mibBuilder.importSymbols('ALCATEL-IND1-BASE','softentIND1LicenseManager')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','TextualConvention')
aluLicenseManagerMIB=ModuleIdentity((1,3,6,1,4,1,6486,800,1,2,1,54,1))
if mibBuilder.loadTexts:aluLicenseManagerMIB.setRevisions(('2009-03-23 00:00','2011-07-14 00:00'))
_AluLicenseManagerMIBNotifications_ObjectIdentity=ObjectIdentity
aluLicenseManagerMIBNotifications=_AluLicenseManagerMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,54,1,0))
_AluLicenseManagerMIBObjects_ObjectIdentity=ObjectIdentity
aluLicenseManagerMIBObjects=_AluLicenseManagerMIBObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,54,1,1))
if mibBuilder.loadTexts:aluLicenseManagerMIBObjects.setStatus(_A)
_AluLicenseManagerConfig_ObjectIdentity=ObjectIdentity
aluLicenseManagerConfig=_AluLicenseManagerConfig_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,1))
class _AluLicenseManagerApplyLicense_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('default',0),('apply',1)))
_AluLicenseManagerApplyLicense_Type.__name__=_C
_AluLicenseManagerApplyLicense_Object=MibScalar
aluLicenseManagerApplyLicense=_AluLicenseManagerApplyLicense_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,1,1),_AluLicenseManagerApplyLicense_Type())
aluLicenseManagerApplyLicense.setMaxAccess(_E)
if mibBuilder.loadTexts:aluLicenseManagerApplyLicense.setStatus(_A)
class _AluLicensedFileName_Type(DisplayString):defaultValue=OctetString('lmlicense.dat');subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AluLicensedFileName_Type.__name__=_F
_AluLicensedFileName_Object=MibScalar
aluLicensedFileName=_AluLicensedFileName_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,1,2),_AluLicensedFileName_Type())
aluLicensedFileName.setMaxAccess(_E)
if mibBuilder.loadTexts:aluLicensedFileName.setStatus(_A)
_AluLicenseManagerInfoTable_Object=MibTable
aluLicenseManagerInfoTable=_AluLicenseManagerInfoTable_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,2))
if mibBuilder.loadTexts:aluLicenseManagerInfoTable.setStatus(_A)
_AluLicenseManagerInfoEntry_Object=MibTableRow
aluLicenseManagerInfoEntry=_AluLicenseManagerInfoEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,2,1))
aluLicenseManagerInfoEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:aluLicenseManagerInfoEntry.setStatus(_A)
class _AluLicenseId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4294967295))
_AluLicenseId_Type.__name__=_H
_AluLicenseId_Object=MibTableColumn
aluLicenseId=_AluLicenseId_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,2,1,1),_AluLicenseId_Type())
aluLicenseId.setMaxAccess(_G)
if mibBuilder.loadTexts:aluLicenseId.setStatus(_A)
class _AluLicensedApplication_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AluLicensedApplication_Type.__name__=_F
_AluLicensedApplication_Object=MibTableColumn
aluLicensedApplication=_AluLicensedApplication_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,2,1,2),_AluLicensedApplication_Type())
aluLicensedApplication.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLicensedApplication.setStatus(_A)
class _AluLicenseType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('demo',1),(_M,2)))
_AluLicenseType_Type.__name__=_C
_AluLicenseType_Object=MibTableColumn
aluLicenseType=_AluLicenseType_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,2,1,3),_AluLicenseType_Type())
aluLicenseType.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLicenseType.setStatus(_A)
class _AluLicenseTimeRemaining_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_AluLicenseTimeRemaining_Type.__name__=_C
_AluLicenseTimeRemaining_Object=MibTableColumn
aluLicenseTimeRemaining=_AluLicenseTimeRemaining_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,2,1,4),_AluLicenseTimeRemaining_Type())
aluLicenseTimeRemaining.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLicenseTimeRemaining.setStatus(_A)
_AluLicenseManagerFileInfoTable_Object=MibTable
aluLicenseManagerFileInfoTable=_AluLicenseManagerFileInfoTable_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,3))
if mibBuilder.loadTexts:aluLicenseManagerFileInfoTable.setStatus(_A)
_AluLicenseManagerFileInfoEntry_Object=MibTableRow
aluLicenseManagerFileInfoEntry=_AluLicenseManagerFileInfoEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,3,1))
aluLicenseManagerFileInfoEntry.setIndexNames((0,_B,_N))
if mibBuilder.loadTexts:aluLicenseManagerFileInfoEntry.setStatus(_A)
class _AluLicenseFileIndex_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_AluLicenseFileIndex_Type.__name__=_H
_AluLicenseFileIndex_Object=MibTableColumn
aluLicenseFileIndex=_AluLicenseFileIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,3,1,1),_AluLicenseFileIndex_Type())
aluLicenseFileIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:aluLicenseFileIndex.setStatus(_A)
_AluSwitchMacAddress_Type=MacAddress
_AluSwitchMacAddress_Object=MibTableColumn
aluSwitchMacAddress=_AluSwitchMacAddress_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,3,1,2),_AluSwitchMacAddress_Type())
aluSwitchMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:aluSwitchMacAddress.setStatus(_A)
class _AluLicensedFileApplication_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AluLicensedFileApplication_Type.__name__=_F
_AluLicensedFileApplication_Object=MibTableColumn
aluLicensedFileApplication=_AluLicensedFileApplication_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,3,1,3),_AluLicensedFileApplication_Type())
aluLicensedFileApplication.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLicensedFileApplication.setStatus(_A)
class _AluLicensedFileLocal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('local',1),('other',2)))
_AluLicensedFileLocal_Type.__name__=_C
_AluLicensedFileLocal_Object=MibTableColumn
aluLicensedFileLocal=_AluLicensedFileLocal_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,3,1,4),_AluLicensedFileLocal_Type())
aluLicensedFileLocal.setMaxAccess(_E)
if mibBuilder.loadTexts:aluLicensedFileLocal.setStatus(_A)
_AluLicenseManagerRemoveTable_Object=MibTable
aluLicenseManagerRemoveTable=_AluLicenseManagerRemoveTable_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,4))
if mibBuilder.loadTexts:aluLicenseManagerRemoveTable.setStatus(_A)
_AluLicenseManagerRemoveEntry_Object=MibTableRow
aluLicenseManagerRemoveEntry=_AluLicenseManagerRemoveEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,4,1))
aluLicenseManagerRemoveEntry.setIndexNames((0,_B,_O))
if mibBuilder.loadTexts:aluLicenseManagerRemoveEntry.setStatus(_A)
class _AluLicenseRemoveIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AluLicenseRemoveIndex_Type.__name__=_C
_AluLicenseRemoveIndex_Object=MibTableColumn
aluLicenseRemoveIndex=_AluLicenseRemoveIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,4,1,1),_AluLicenseRemoveIndex_Type())
aluLicenseRemoveIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:aluLicenseRemoveIndex.setStatus(_A)
class _AluLicenseRemoveFeatureID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('metro',1),(_P,2),(_Q,3)))
_AluLicenseRemoveFeatureID_Type.__name__=_C
_AluLicenseRemoveFeatureID_Object=MibTableColumn
aluLicenseRemoveFeatureID=_AluLicenseRemoveFeatureID_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,4,1,2),_AluLicenseRemoveFeatureID_Type())
aluLicenseRemoveFeatureID.setMaxAccess(_E)
if mibBuilder.loadTexts:aluLicenseRemoveFeatureID.setStatus(_A)
class _AluLicenseRemoveSlotID_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1008))
_AluLicenseRemoveSlotID_Type.__name__=_C
_AluLicenseRemoveSlotID_Object=MibTableColumn
aluLicenseRemoveSlotID=_AluLicenseRemoveSlotID_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,4,1,3),_AluLicenseRemoveSlotID_Type())
aluLicenseRemoveSlotID.setMaxAccess(_E)
if mibBuilder.loadTexts:aluLicenseRemoveSlotID.setStatus(_A)
_AluLicenseManagerDemoLicenseTable_Object=MibTable
aluLicenseManagerDemoLicenseTable=_AluLicenseManagerDemoLicenseTable_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,5))
if mibBuilder.loadTexts:aluLicenseManagerDemoLicenseTable.setStatus(_A)
_AluLicenseManagerDemoLicenseEntry_Object=MibTableRow
aluLicenseManagerDemoLicenseEntry=_AluLicenseManagerDemoLicenseEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,5,1))
aluLicenseManagerDemoLicenseEntry.setIndexNames((0,_B,_R))
if mibBuilder.loadTexts:aluLicenseManagerDemoLicenseEntry.setStatus(_A)
class _AluLicenseDemoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AluLicenseDemoIndex_Type.__name__=_C
_AluLicenseDemoIndex_Object=MibTableColumn
aluLicenseDemoIndex=_AluLicenseDemoIndex_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,5,1,1),_AluLicenseDemoIndex_Type())
aluLicenseDemoIndex.setMaxAccess(_G)
if mibBuilder.loadTexts:aluLicenseDemoIndex.setStatus(_A)
class _AluLicenseDemoFeatureID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('metro',1),(_P,2),(_Q,3)))
_AluLicenseDemoFeatureID_Type.__name__=_C
_AluLicenseDemoFeatureID_Object=MibTableColumn
aluLicenseDemoFeatureID=_AluLicenseDemoFeatureID_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,5,1,2),_AluLicenseDemoFeatureID_Type())
aluLicenseDemoFeatureID.setMaxAccess(_E)
if mibBuilder.loadTexts:aluLicenseDemoFeatureID.setStatus(_A)
class _AluLicenseDemoSlotID_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1008))
_AluLicenseDemoSlotID_Type.__name__=_C
_AluLicenseDemoSlotID_Object=MibTableColumn
aluLicenseDemoSlotID=_AluLicenseDemoSlotID_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,5,1,3),_AluLicenseDemoSlotID_Type())
aluLicenseDemoSlotID.setMaxAccess(_E)
if mibBuilder.loadTexts:aluLicenseDemoSlotID.setStatus(_A)
_AluLicenseManagerLicenseInfoTable_Object=MibTable
aluLicenseManagerLicenseInfoTable=_AluLicenseManagerLicenseInfoTable_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,6))
if mibBuilder.loadTexts:aluLicenseManagerLicenseInfoTable.setStatus(_A)
_AluLicenseManagerLicenseInfoEntry_Object=MibTableRow
aluLicenseManagerLicenseInfoEntry=_AluLicenseManagerLicenseInfoEntry_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,6,1))
aluLicenseManagerLicenseInfoEntry.setIndexNames((0,_B,_S),(0,_B,_T))
if mibBuilder.loadTexts:aluLicenseManagerLicenseInfoEntry.setStatus(_A)
class _AluLicenseInfoSlotId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1008))
_AluLicenseInfoSlotId_Type.__name__=_H
_AluLicenseInfoSlotId_Object=MibTableColumn
aluLicenseInfoSlotId=_AluLicenseInfoSlotId_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,6,1,1),_AluLicenseInfoSlotId_Type())
aluLicenseInfoSlotId.setMaxAccess(_G)
if mibBuilder.loadTexts:aluLicenseInfoSlotId.setStatus(_A)
class _AluLicensedInfoApplication_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AluLicensedInfoApplication_Type.__name__=_F
_AluLicensedInfoApplication_Object=MibTableColumn
aluLicensedInfoApplication=_AluLicensedInfoApplication_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,6,1,2),_AluLicensedInfoApplication_Type())
aluLicensedInfoApplication.setMaxAccess(_G)
if mibBuilder.loadTexts:aluLicensedInfoApplication.setStatus(_A)
class _AluLicenseInfoType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('demo',1),(_M,2)))
_AluLicenseInfoType_Type.__name__=_C
_AluLicenseInfoType_Object=MibTableColumn
aluLicenseInfoType=_AluLicenseInfoType_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,6,1,3),_AluLicenseInfoType_Type())
aluLicenseInfoType.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLicenseInfoType.setStatus(_A)
class _AluLicenseInfoTimeRemaining_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60))
_AluLicenseInfoTimeRemaining_Type.__name__=_C
_AluLicenseInfoTimeRemaining_Object=MibTableColumn
aluLicenseInfoTimeRemaining=_AluLicenseInfoTimeRemaining_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,1,6,1,4),_AluLicenseInfoTimeRemaining_Type())
aluLicenseInfoTimeRemaining.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLicenseInfoTimeRemaining.setStatus(_A)
_AluLicenseManagerMIBConformance_ObjectIdentity=ObjectIdentity
aluLicenseManagerMIBConformance=_AluLicenseManagerMIBConformance_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,54,1,2))
if mibBuilder.loadTexts:aluLicenseManagerMIBConformance.setStatus(_A)
_AluLicenseManagerMIBGroups_ObjectIdentity=ObjectIdentity
aluLicenseManagerMIBGroups=_AluLicenseManagerMIBGroups_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,54,1,2,1))
if mibBuilder.loadTexts:aluLicenseManagerMIBGroups.setStatus(_A)
_AluLicenseManagerMIBCompliances_ObjectIdentity=ObjectIdentity
aluLicenseManagerMIBCompliances=_AluLicenseManagerMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,54,1,2,2))
if mibBuilder.loadTexts:aluLicenseManagerMIBCompliances.setStatus(_A)
_AluLicenseManagerMIBTrapObjects_ObjectIdentity=ObjectIdentity
aluLicenseManagerMIBTrapObjects=_AluLicenseManagerMIBTrapObjects_ObjectIdentity((1,3,6,1,4,1,6486,800,1,2,1,54,1,3))
class _AluLicensedInfoSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1008))
_AluLicensedInfoSlot_Type.__name__=_C
_AluLicensedInfoSlot_Object=MibScalar
aluLicensedInfoSlot=_AluLicensedInfoSlot_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,3,1),_AluLicensedInfoSlot_Type())
aluLicensedInfoSlot.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLicensedInfoSlot.setStatus(_A)
class _AluLicenseInfoFeature_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_AluLicenseInfoFeature_Type.__name__=_F
_AluLicenseInfoFeature_Object=MibScalar
aluLicenseInfoFeature=_AluLicenseInfoFeature_Object((1,3,6,1,4,1,6486,800,1,2,1,54,1,3,2),_AluLicenseInfoFeature_Type())
aluLicenseInfoFeature.setMaxAccess(_D)
if mibBuilder.loadTexts:aluLicenseInfoFeature.setStatus(_A)
aluLicenseManagerConfigGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,54,1,2,1,1))
aluLicenseManagerConfigGroup.setObjects(*((_B,_U),(_B,_V)))
if mibBuilder.loadTexts:aluLicenseManagerConfigGroup.setStatus(_A)
aluLicenseManagerInfoGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,54,1,2,1,2))
aluLicenseManagerInfoGroup.setObjects(*((_B,_I),(_B,_W),(_B,_J)))
if mibBuilder.loadTexts:aluLicenseManagerInfoGroup.setStatus(_A)
aluLicenseManagerFileInfoGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,54,1,2,1,4))
aluLicenseManagerFileInfoGroup.setObjects(*((_B,_X),(_B,_Y),(_B,_Z)))
if mibBuilder.loadTexts:aluLicenseManagerFileInfoGroup.setStatus(_A)
aluLicenseManagerRemoveInfoGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,54,1,2,1,5))
aluLicenseManagerRemoveInfoGroup.setObjects(*((_B,_a),(_B,_b)))
if mibBuilder.loadTexts:aluLicenseManagerRemoveInfoGroup.setStatus(_A)
aluLicenseManagerDemoInfoGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,54,1,2,1,6))
aluLicenseManagerDemoInfoGroup.setObjects(*((_B,_c),(_B,_d)))
if mibBuilder.loadTexts:aluLicenseManagerDemoInfoGroup.setStatus(_A)
aluLicenseManagerLicenseInfoGroup=ObjectGroup((1,3,6,1,4,1,6486,800,1,2,1,54,1,2,1,7))
aluLicenseManagerLicenseInfoGroup.setObjects(*((_B,_e),(_B,_K)))
if mibBuilder.loadTexts:aluLicenseManagerLicenseInfoGroup.setStatus(_A)
aluLicenseManagerLicenseExpired=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,54,1,0,0,1))
aluLicenseManagerLicenseExpired.setObjects(*((_B,_I),(_B,_J)))
if mibBuilder.loadTexts:aluLicenseManagerLicenseExpired.setStatus(_A)
aluLicenseManagerLicenseExpiry=NotificationType((1,3,6,1,4,1,6486,800,1,2,1,54,1,0,0,2))
aluLicenseManagerLicenseExpiry.setObjects(*((_B,_f),(_B,_K),(_B,_g)))
if mibBuilder.loadTexts:aluLicenseManagerLicenseExpiry.setStatus(_A)
aluLicenseManagerNotificationsGroup=NotificationGroup((1,3,6,1,4,1,6486,800,1,2,1,54,1,2,1,3))
aluLicenseManagerNotificationsGroup.setObjects(*((_B,_h),(_B,_i)))
if mibBuilder.loadTexts:aluLicenseManagerNotificationsGroup.setStatus(_A)
aluLicenseManagerMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6486,800,1,2,1,54,1,2,2,1))
aluLicenseManagerMIBCompliance.setObjects(*((_B,_j),(_B,_k),(_B,_l),(_B,_m),(_B,_n),(_B,_o),(_B,_p)))
if mibBuilder.loadTexts:aluLicenseManagerMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'aluLicenseManagerMIB':aluLicenseManagerMIB,'aluLicenseManagerMIBNotifications':aluLicenseManagerMIBNotifications,_h:aluLicenseManagerLicenseExpired,_i:aluLicenseManagerLicenseExpiry,'aluLicenseManagerMIBObjects':aluLicenseManagerMIBObjects,'aluLicenseManagerConfig':aluLicenseManagerConfig,_U:aluLicenseManagerApplyLicense,_V:aluLicensedFileName,'aluLicenseManagerInfoTable':aluLicenseManagerInfoTable,'aluLicenseManagerInfoEntry':aluLicenseManagerInfoEntry,_L:aluLicenseId,_I:aluLicensedApplication,_W:aluLicenseType,_J:aluLicenseTimeRemaining,'aluLicenseManagerFileInfoTable':aluLicenseManagerFileInfoTable,'aluLicenseManagerFileInfoEntry':aluLicenseManagerFileInfoEntry,_N:aluLicenseFileIndex,_X:aluSwitchMacAddress,_Y:aluLicensedFileApplication,_Z:aluLicensedFileLocal,'aluLicenseManagerRemoveTable':aluLicenseManagerRemoveTable,'aluLicenseManagerRemoveEntry':aluLicenseManagerRemoveEntry,_O:aluLicenseRemoveIndex,_a:aluLicenseRemoveFeatureID,_b:aluLicenseRemoveSlotID,'aluLicenseManagerDemoLicenseTable':aluLicenseManagerDemoLicenseTable,'aluLicenseManagerDemoLicenseEntry':aluLicenseManagerDemoLicenseEntry,_R:aluLicenseDemoIndex,_c:aluLicenseDemoFeatureID,_d:aluLicenseDemoSlotID,'aluLicenseManagerLicenseInfoTable':aluLicenseManagerLicenseInfoTable,'aluLicenseManagerLicenseInfoEntry':aluLicenseManagerLicenseInfoEntry,_S:aluLicenseInfoSlotId,_T:aluLicensedInfoApplication,_e:aluLicenseInfoType,_K:aluLicenseInfoTimeRemaining,'aluLicenseManagerMIBConformance':aluLicenseManagerMIBConformance,'aluLicenseManagerMIBGroups':aluLicenseManagerMIBGroups,_j:aluLicenseManagerConfigGroup,_p:aluLicenseManagerInfoGroup,_l:aluLicenseManagerNotificationsGroup,_m:aluLicenseManagerFileInfoGroup,_n:aluLicenseManagerRemoveInfoGroup,_o:aluLicenseManagerDemoInfoGroup,_k:aluLicenseManagerLicenseInfoGroup,'aluLicenseManagerMIBCompliances':aluLicenseManagerMIBCompliances,'aluLicenseManagerMIBCompliance':aluLicenseManagerMIBCompliance,'aluLicenseManagerMIBTrapObjects':aluLicenseManagerMIBTrapObjects,_g:aluLicensedInfoSlot,_f:aluLicenseInfoFeature})