_w='vmwVmInfoNotificationGroup'
_v='vmwVmInfoGroup'
_u='vmwVmSuspended'
_t='vmwVmHBDetected'
_s='vmwVmHBLost'
_r='vmwVmPoweredOff'
_q='vmwVmPoweredOn'
_p='vmwVmNetConnType'
_o='vmwVmVMID'
_n='vmwVmUUID'
_m='vmwVmCpus'
_l='vmwCdromConnected'
_k='vmwCdromName'
_j='vmwFdConnected'
_i='vmwFdName'
_h='vmwVmMAC'
_g='vmwVmNetConnected'
_f='vmwVmNetName'
_e='vmwVmNetNum'
_d='vmwHbaTgtNum'
_c='vmwHbaVirtDev'
_b='vmwHbaNum'
_a='vmwVmGuestState'
_Z='vmwVmState'
_Y='vmwVmMemSize'
_X='vmwVmGuestOS'
_W='vmwVmConfigFile'
_V='accessible-for-notify'
_U='vmwCdromIdx'
_T='vmwCdVmIdx'
_S='vmwFdIdx'
_R='vmwFdVmIdx'
_Q='vmwVmNetIdx'
_P='vmwVmNetVmIdx'
_O='vmwHbaTgtIdx'
_N='vmwHbaTgtVmIdx'
_M='vmwVmHbaIdx'
_L='vmwHbaVmIdx'
_K='vmwVmIdx'
_J='OctetString'
_I='obsolete'
_H='vmwVmConfigFilePath'
_G='vmwVmID'
_F='vmwVmDisplayName'
_E='not-accessible'
_D='Integer32'
_C='read-only'
_B='current'
_A='VMWARE-VMINFO-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_J,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vmwESXNotifications,=mibBuilder.importSymbols('VMWARE-ENV-MIB','vmwESXNotifications')
vmwTraps,vmwVirtMachines=mibBuilder.importSymbols('VMWARE-ROOT-MIB','vmwTraps','vmwVirtMachines')
VmwConnectedState,=mibBuilder.importSymbols('VMWARE-TC-MIB','VmwConnectedState')
vmwVmInfoMIB=ModuleIdentity((1,3,6,1,4,1,6876,2,10))
if mibBuilder.loadTexts:vmwVmInfoMIB.setRevisions(('2011-09-17 00:00','2010-06-22 00:00','2008-10-23 00:00','2007-12-27 00:00'))
_VmwVmTable_Object=MibTable
vmwVmTable=_VmwVmTable_Object((1,3,6,1,4,1,6876,2,1))
if mibBuilder.loadTexts:vmwVmTable.setStatus(_B)
_VmwVmEntry_Object=MibTableRow
vmwVmEntry=_VmwVmEntry_Object((1,3,6,1,4,1,6876,2,1,1))
vmwVmEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:vmwVmEntry.setStatus(_B)
class _VmwVmIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VmwVmIdx_Type.__name__=_D
_VmwVmIdx_Object=MibTableColumn
vmwVmIdx=_VmwVmIdx_Object((1,3,6,1,4,1,6876,2,1,1,1),_VmwVmIdx_Type())
vmwVmIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:vmwVmIdx.setStatus(_B)
_VmwVmDisplayName_Type=DisplayString
_VmwVmDisplayName_Object=MibTableColumn
vmwVmDisplayName=_VmwVmDisplayName_Object((1,3,6,1,4,1,6876,2,1,1,2),_VmwVmDisplayName_Type())
vmwVmDisplayName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVmDisplayName.setStatus(_B)
_VmwVmConfigFile_Type=DisplayString
_VmwVmConfigFile_Object=MibTableColumn
vmwVmConfigFile=_VmwVmConfigFile_Object((1,3,6,1,4,1,6876,2,1,1,3),_VmwVmConfigFile_Type())
vmwVmConfigFile.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVmConfigFile.setStatus(_B)
_VmwVmGuestOS_Type=DisplayString
_VmwVmGuestOS_Object=MibTableColumn
vmwVmGuestOS=_VmwVmGuestOS_Object((1,3,6,1,4,1,6876,2,1,1,4),_VmwVmGuestOS_Type())
vmwVmGuestOS.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVmGuestOS.setStatus(_B)
_VmwVmMemSize_Type=Integer32
_VmwVmMemSize_Object=MibTableColumn
vmwVmMemSize=_VmwVmMemSize_Object((1,3,6,1,4,1,6876,2,1,1,5),_VmwVmMemSize_Type())
vmwVmMemSize.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVmMemSize.setStatus(_B)
if mibBuilder.loadTexts:vmwVmMemSize.setUnits('megabytes')
_VmwVmState_Type=DisplayString
_VmwVmState_Object=MibTableColumn
vmwVmState=_VmwVmState_Object((1,3,6,1,4,1,6876,2,1,1,6),_VmwVmState_Type())
vmwVmState.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVmState.setStatus(_B)
_VmwVmVMID_Type=Integer32
_VmwVmVMID_Object=MibTableColumn
vmwVmVMID=_VmwVmVMID_Object((1,3,6,1,4,1,6876,2,1,1,7),_VmwVmVMID_Type())
vmwVmVMID.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVmVMID.setStatus(_I)
_VmwVmGuestState_Type=DisplayString
_VmwVmGuestState_Object=MibTableColumn
vmwVmGuestState=_VmwVmGuestState_Object((1,3,6,1,4,1,6876,2,1,1,8),_VmwVmGuestState_Type())
vmwVmGuestState.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVmGuestState.setStatus(_B)
_VmwVmCpus_Type=Integer32
_VmwVmCpus_Object=MibTableColumn
vmwVmCpus=_VmwVmCpus_Object((1,3,6,1,4,1,6876,2,1,1,9),_VmwVmCpus_Type())
vmwVmCpus.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVmCpus.setStatus(_B)
class _VmwVmUUID_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(36,72))
_VmwVmUUID_Type.__name__=_J
_VmwVmUUID_Object=MibTableColumn
vmwVmUUID=_VmwVmUUID_Object((1,3,6,1,4,1,6876,2,1,1,10),_VmwVmUUID_Type())
vmwVmUUID.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVmUUID.setStatus(_B)
_VmwVmHbaTable_Object=MibTable
vmwVmHbaTable=_VmwVmHbaTable_Object((1,3,6,1,4,1,6876,2,2))
if mibBuilder.loadTexts:vmwVmHbaTable.setStatus(_B)
_VmwVmHbaEntry_Object=MibTableRow
vmwVmHbaEntry=_VmwVmHbaEntry_Object((1,3,6,1,4,1,6876,2,2,1))
vmwVmHbaEntry.setIndexNames((0,_A,_L),(0,_A,_M))
if mibBuilder.loadTexts:vmwVmHbaEntry.setStatus(_B)
class _VmwHbaVmIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VmwHbaVmIdx_Type.__name__=_D
_VmwHbaVmIdx_Object=MibTableColumn
vmwHbaVmIdx=_VmwHbaVmIdx_Object((1,3,6,1,4,1,6876,2,2,1,1),_VmwHbaVmIdx_Type())
vmwHbaVmIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:vmwHbaVmIdx.setStatus(_B)
class _VmwVmHbaIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VmwVmHbaIdx_Type.__name__=_D
_VmwVmHbaIdx_Object=MibTableColumn
vmwVmHbaIdx=_VmwVmHbaIdx_Object((1,3,6,1,4,1,6876,2,2,1,2),_VmwVmHbaIdx_Type())
vmwVmHbaIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:vmwVmHbaIdx.setStatus(_B)
_VmwHbaNum_Type=DisplayString
_VmwHbaNum_Object=MibTableColumn
vmwHbaNum=_VmwHbaNum_Object((1,3,6,1,4,1,6876,2,2,1,3),_VmwHbaNum_Type())
vmwHbaNum.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwHbaNum.setStatus(_B)
_VmwHbaVirtDev_Type=DisplayString
_VmwHbaVirtDev_Object=MibTableColumn
vmwHbaVirtDev=_VmwHbaVirtDev_Object((1,3,6,1,4,1,6876,2,2,1,4),_VmwHbaVirtDev_Type())
vmwHbaVirtDev.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwHbaVirtDev.setStatus(_B)
_VmwHbaTgtTable_Object=MibTable
vmwHbaTgtTable=_VmwHbaTgtTable_Object((1,3,6,1,4,1,6876,2,3))
if mibBuilder.loadTexts:vmwHbaTgtTable.setStatus(_B)
_VmwHbaTgtEntry_Object=MibTableRow
vmwHbaTgtEntry=_VmwHbaTgtEntry_Object((1,3,6,1,4,1,6876,2,3,1))
vmwHbaTgtEntry.setIndexNames((0,_A,_N),(0,_A,_O))
if mibBuilder.loadTexts:vmwHbaTgtEntry.setStatus(_B)
class _VmwHbaTgtVmIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VmwHbaTgtVmIdx_Type.__name__=_D
_VmwHbaTgtVmIdx_Object=MibTableColumn
vmwHbaTgtVmIdx=_VmwHbaTgtVmIdx_Object((1,3,6,1,4,1,6876,2,3,1,1),_VmwHbaTgtVmIdx_Type())
vmwHbaTgtVmIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:vmwHbaTgtVmIdx.setStatus(_B)
class _VmwHbaTgtIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VmwHbaTgtIdx_Type.__name__=_D
_VmwHbaTgtIdx_Object=MibTableColumn
vmwHbaTgtIdx=_VmwHbaTgtIdx_Object((1,3,6,1,4,1,6876,2,3,1,2),_VmwHbaTgtIdx_Type())
vmwHbaTgtIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:vmwHbaTgtIdx.setStatus(_B)
_VmwHbaTgtNum_Type=DisplayString
_VmwHbaTgtNum_Object=MibTableColumn
vmwHbaTgtNum=_VmwHbaTgtNum_Object((1,3,6,1,4,1,6876,2,3,1,3),_VmwHbaTgtNum_Type())
vmwHbaTgtNum.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwHbaTgtNum.setStatus(_B)
_VmwVmNetTable_Object=MibTable
vmwVmNetTable=_VmwVmNetTable_Object((1,3,6,1,4,1,6876,2,4))
if mibBuilder.loadTexts:vmwVmNetTable.setStatus(_B)
_VmwVmNetEntry_Object=MibTableRow
vmwVmNetEntry=_VmwVmNetEntry_Object((1,3,6,1,4,1,6876,2,4,1))
vmwVmNetEntry.setIndexNames((0,_A,_P),(0,_A,_Q))
if mibBuilder.loadTexts:vmwVmNetEntry.setStatus(_B)
class _VmwVmNetVmIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VmwVmNetVmIdx_Type.__name__=_D
_VmwVmNetVmIdx_Object=MibTableColumn
vmwVmNetVmIdx=_VmwVmNetVmIdx_Object((1,3,6,1,4,1,6876,2,4,1,1),_VmwVmNetVmIdx_Type())
vmwVmNetVmIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:vmwVmNetVmIdx.setStatus(_B)
class _VmwVmNetIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VmwVmNetIdx_Type.__name__=_D
_VmwVmNetIdx_Object=MibTableColumn
vmwVmNetIdx=_VmwVmNetIdx_Object((1,3,6,1,4,1,6876,2,4,1,2),_VmwVmNetIdx_Type())
vmwVmNetIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:vmwVmNetIdx.setStatus(_B)
_VmwVmNetNum_Type=DisplayString
_VmwVmNetNum_Object=MibTableColumn
vmwVmNetNum=_VmwVmNetNum_Object((1,3,6,1,4,1,6876,2,4,1,3),_VmwVmNetNum_Type())
vmwVmNetNum.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVmNetNum.setStatus(_B)
_VmwVmNetName_Type=DisplayString
_VmwVmNetName_Object=MibTableColumn
vmwVmNetName=_VmwVmNetName_Object((1,3,6,1,4,1,6876,2,4,1,4),_VmwVmNetName_Type())
vmwVmNetName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVmNetName.setStatus(_B)
_VmwVmNetConnType_Type=DisplayString
_VmwVmNetConnType_Object=MibTableColumn
vmwVmNetConnType=_VmwVmNetConnType_Object((1,3,6,1,4,1,6876,2,4,1,5),_VmwVmNetConnType_Type())
vmwVmNetConnType.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVmNetConnType.setStatus(_I)
_VmwVmNetConnected_Type=VmwConnectedState
_VmwVmNetConnected_Object=MibTableColumn
vmwVmNetConnected=_VmwVmNetConnected_Object((1,3,6,1,4,1,6876,2,4,1,6),_VmwVmNetConnected_Type())
vmwVmNetConnected.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVmNetConnected.setStatus(_B)
_VmwVmMAC_Type=PhysAddress
_VmwVmMAC_Object=MibTableColumn
vmwVmMAC=_VmwVmMAC_Object((1,3,6,1,4,1,6876,2,4,1,7),_VmwVmMAC_Type())
vmwVmMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwVmMAC.setStatus(_B)
_VmwFloppyTable_Object=MibTable
vmwFloppyTable=_VmwFloppyTable_Object((1,3,6,1,4,1,6876,2,5))
if mibBuilder.loadTexts:vmwFloppyTable.setStatus(_B)
_VmwFloppyEntry_Object=MibTableRow
vmwFloppyEntry=_VmwFloppyEntry_Object((1,3,6,1,4,1,6876,2,5,1))
vmwFloppyEntry.setIndexNames((0,_A,_R),(0,_A,_S))
if mibBuilder.loadTexts:vmwFloppyEntry.setStatus(_B)
class _VmwFdVmIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VmwFdVmIdx_Type.__name__=_D
_VmwFdVmIdx_Object=MibTableColumn
vmwFdVmIdx=_VmwFdVmIdx_Object((1,3,6,1,4,1,6876,2,5,1,1),_VmwFdVmIdx_Type())
vmwFdVmIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:vmwFdVmIdx.setStatus(_B)
class _VmwFdIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VmwFdIdx_Type.__name__=_D
_VmwFdIdx_Object=MibTableColumn
vmwFdIdx=_VmwFdIdx_Object((1,3,6,1,4,1,6876,2,5,1,2),_VmwFdIdx_Type())
vmwFdIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:vmwFdIdx.setStatus(_B)
_VmwFdName_Type=DisplayString
_VmwFdName_Object=MibTableColumn
vmwFdName=_VmwFdName_Object((1,3,6,1,4,1,6876,2,5,1,3),_VmwFdName_Type())
vmwFdName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwFdName.setStatus(_B)
_VmwFdConnected_Type=VmwConnectedState
_VmwFdConnected_Object=MibTableColumn
vmwFdConnected=_VmwFdConnected_Object((1,3,6,1,4,1,6876,2,5,1,4),_VmwFdConnected_Type())
vmwFdConnected.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwFdConnected.setStatus(_B)
_VmwCdromTable_Object=MibTable
vmwCdromTable=_VmwCdromTable_Object((1,3,6,1,4,1,6876,2,6))
if mibBuilder.loadTexts:vmwCdromTable.setStatus(_B)
_VmwCdromEntry_Object=MibTableRow
vmwCdromEntry=_VmwCdromEntry_Object((1,3,6,1,4,1,6876,2,6,1))
vmwCdromEntry.setIndexNames((0,_A,_T),(0,_A,_U))
if mibBuilder.loadTexts:vmwCdromEntry.setStatus(_B)
class _VmwCdVmIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VmwCdVmIdx_Type.__name__=_D
_VmwCdVmIdx_Object=MibTableColumn
vmwCdVmIdx=_VmwCdVmIdx_Object((1,3,6,1,4,1,6876,2,6,1,1),_VmwCdVmIdx_Type())
vmwCdVmIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:vmwCdVmIdx.setStatus(_B)
class _VmwCdromIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_VmwCdromIdx_Type.__name__=_D
_VmwCdromIdx_Object=MibTableColumn
vmwCdromIdx=_VmwCdromIdx_Object((1,3,6,1,4,1,6876,2,6,1,2),_VmwCdromIdx_Type())
vmwCdromIdx.setMaxAccess(_E)
if mibBuilder.loadTexts:vmwCdromIdx.setStatus(_B)
_VmwCdromName_Type=DisplayString
_VmwCdromName_Object=MibTableColumn
vmwCdromName=_VmwCdromName_Object((1,3,6,1,4,1,6876,2,6,1,3),_VmwCdromName_Type())
vmwCdromName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwCdromName.setStatus(_B)
_VmwCdromConnected_Type=VmwConnectedState
_VmwCdromConnected_Object=MibTableColumn
vmwCdromConnected=_VmwCdromConnected_Object((1,3,6,1,4,1,6876,2,6,1,4),_VmwCdromConnected_Type())
vmwCdromConnected.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwCdromConnected.setStatus(_B)
_VmwVmInfoMIBConformance_ObjectIdentity=ObjectIdentity
vmwVmInfoMIBConformance=_VmwVmInfoMIBConformance_ObjectIdentity((1,3,6,1,4,1,6876,2,10,2))
_VmwVmInfoMIBCompliances_ObjectIdentity=ObjectIdentity
vmwVmInfoMIBCompliances=_VmwVmInfoMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6876,2,10,2,1))
_VmwVmInfoMIBGroups_ObjectIdentity=ObjectIdentity
vmwVmInfoMIBGroups=_VmwVmInfoMIBGroups_ObjectIdentity((1,3,6,1,4,1,6876,2,10,2,2))
_VmwVmID_Type=Integer32
_VmwVmID_Object=MibScalar
vmwVmID=_VmwVmID_Object((1,3,6,1,4,1,6876,50,101),_VmwVmID_Type())
vmwVmID.setMaxAccess(_V)
if mibBuilder.loadTexts:vmwVmID.setStatus(_B)
_VmwVmConfigFilePath_Type=DisplayString
_VmwVmConfigFilePath_Object=MibScalar
vmwVmConfigFilePath=_VmwVmConfigFilePath_Object((1,3,6,1,4,1,6876,50,102),_VmwVmConfigFilePath_Type())
vmwVmConfigFilePath.setMaxAccess(_V)
if mibBuilder.loadTexts:vmwVmConfigFilePath.setStatus(_B)
vmwVmInfoGroup=ObjectGroup((1,3,6,1,4,1,6876,2,10,2,2,1))
vmwVmInfoGroup.setObjects(*((_A,_F),(_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_G),(_A,_H),(_A,_m),(_A,_n)))
if mibBuilder.loadTexts:vmwVmInfoGroup.setStatus(_B)
vmwVmObsoleteGroup=ObjectGroup((1,3,6,1,4,1,6876,2,10,2,2,3))
vmwVmObsoleteGroup.setObjects(*((_A,_o),(_A,_p)))
if mibBuilder.loadTexts:vmwVmObsoleteGroup.setStatus(_I)
vmwVmPoweredOn=NotificationType((1,3,6,1,4,1,6876,4,1,0,1))
vmwVmPoweredOn.setObjects(*((_A,_G),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:vmwVmPoweredOn.setStatus(_B)
vmwVmPoweredOff=NotificationType((1,3,6,1,4,1,6876,4,1,0,2))
vmwVmPoweredOff.setObjects(*((_A,_G),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:vmwVmPoweredOff.setStatus(_B)
vmwVmHBLost=NotificationType((1,3,6,1,4,1,6876,4,1,0,3))
vmwVmHBLost.setObjects(*((_A,_G),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:vmwVmHBLost.setStatus(_B)
vmwVmHBDetected=NotificationType((1,3,6,1,4,1,6876,4,1,0,4))
vmwVmHBDetected.setObjects(*((_A,_G),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:vmwVmHBDetected.setStatus(_B)
vmwVmSuspended=NotificationType((1,3,6,1,4,1,6876,4,1,0,5))
vmwVmSuspended.setObjects(*((_A,_G),(_A,_H),(_A,_F)))
if mibBuilder.loadTexts:vmwVmSuspended.setStatus(_B)
vmwVmInfoNotificationGroup=NotificationGroup((1,3,6,1,4,1,6876,2,10,2,2,2))
vmwVmInfoNotificationGroup.setObjects(*((_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u)))
if mibBuilder.loadTexts:vmwVmInfoNotificationGroup.setStatus(_B)
vmwResMIBBasicCompliance=ModuleCompliance((1,3,6,1,4,1,6876,2,10,2,1,2))
vmwResMIBBasicCompliance.setObjects(*((_A,_v),(_A,_w)))
if mibBuilder.loadTexts:vmwResMIBBasicCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'vmwVmTable':vmwVmTable,'vmwVmEntry':vmwVmEntry,_K:vmwVmIdx,_F:vmwVmDisplayName,_W:vmwVmConfigFile,_X:vmwVmGuestOS,_Y:vmwVmMemSize,_Z:vmwVmState,_o:vmwVmVMID,_a:vmwVmGuestState,_m:vmwVmCpus,_n:vmwVmUUID,'vmwVmHbaTable':vmwVmHbaTable,'vmwVmHbaEntry':vmwVmHbaEntry,_L:vmwHbaVmIdx,_M:vmwVmHbaIdx,_b:vmwHbaNum,_c:vmwHbaVirtDev,'vmwHbaTgtTable':vmwHbaTgtTable,'vmwHbaTgtEntry':vmwHbaTgtEntry,_N:vmwHbaTgtVmIdx,_O:vmwHbaTgtIdx,_d:vmwHbaTgtNum,'vmwVmNetTable':vmwVmNetTable,'vmwVmNetEntry':vmwVmNetEntry,_P:vmwVmNetVmIdx,_Q:vmwVmNetIdx,_e:vmwVmNetNum,_f:vmwVmNetName,_p:vmwVmNetConnType,_g:vmwVmNetConnected,_h:vmwVmMAC,'vmwFloppyTable':vmwFloppyTable,'vmwFloppyEntry':vmwFloppyEntry,_R:vmwFdVmIdx,_S:vmwFdIdx,_i:vmwFdName,_j:vmwFdConnected,'vmwCdromTable':vmwCdromTable,'vmwCdromEntry':vmwCdromEntry,_T:vmwCdVmIdx,_U:vmwCdromIdx,_k:vmwCdromName,_l:vmwCdromConnected,'vmwVmInfoMIB':vmwVmInfoMIB,'vmwVmInfoMIBConformance':vmwVmInfoMIBConformance,'vmwVmInfoMIBCompliances':vmwVmInfoMIBCompliances,'vmwResMIBBasicCompliance':vmwResMIBBasicCompliance,'vmwVmInfoMIBGroups':vmwVmInfoMIBGroups,_v:vmwVmInfoGroup,_w:vmwVmInfoNotificationGroup,'vmwVmObsoleteGroup':vmwVmObsoleteGroup,_q:vmwVmPoweredOn,_r:vmwVmPoweredOff,_s:vmwVmHBLost,_t:vmwVmHBDetected,_u:vmwVmSuspended,_G:vmwVmID,_H:vmwVmConfigFilePath})