_A2='vmwOldVCNotificationGroup'
_A1='vmwObsoleteGroup'
_A0='vmSuspended'
_z='vmHBDetected'
_y='vmHBLost'
_x='vmPoweredOff'
_w='vmPoweredOn'
_v='vpxdTrap'
_u='vmwNetHCKbRx'
_t='vmwNetHCPktsRx'
_s='vmwNetHCKbTx'
_r='vmwNetHCPktsTx'
_q='vmwNetKbRx'
_p='vmwNetPktsRx'
_o='vmwNetKbTx'
_n='vmwNetPktsTx'
_m='vmwNetShares'
_l='vmwNetIfAddr'
_k='vmwNetVMID'
_j='vmwNetName'
_i='vmwKbWritten'
_h='vmwNumWrites'
_g='vmwKbRead'
_f='vmwNumReads'
_e='vmwDiskShares'
_d='vmwHbaVMID'
_c='vmwHbaName'
_b='vmwMemUtil'
_a='vmwMemConfigured'
_Z='vmwMemShares'
_Y='vmwCpuUtil'
_X='vmwCpuShares'
_W='vmkLoaded'
_V='vmwNetIdx'
_U='vmwHbaIdx'
_T='kilobytes'
_S='vmwMemVMID'
_R='unknown'
_Q='vmwCpuVMID'
_P='vpxdObjValue'
_O='vpxdNewStatus'
_N='vpxdOldStatus'
_M='vpxdVMName'
_L='vpxdHostName'
_K='vpxdTrapType'
_J='not-accessible'
_I='Integer32'
_H='accessible-for-notify'
_G='vmwVmID'
_F='vmwVmConfigFilePath'
_E='current'
_D='VMWARE-VMINFO-MIB'
_C='read-only'
_B='obsolete'
_A='VMWARE-OBSOLETE-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_I,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vmwESX,=mibBuilder.importSymbols('VMWARE-PRODUCTS-MIB','vmwESX')
vmwCPU,vmwMemory=mibBuilder.importSymbols('VMWARE-RESOURCES-MIB','vmwCPU','vmwMemory')
vmwNotifications,vmwObsolete,vmwResources,vmwTraps=mibBuilder.importSymbols('VMWARE-ROOT-MIB','vmwNotifications','vmwObsolete','vmwResources','vmwTraps')
vmwVmConfigFilePath,vmwVmID=mibBuilder.importSymbols(_D,_F,_G)
vmwObsoleteMIB=ModuleIdentity((1,3,6,1,4,1,6876,800,1))
if mibBuilder.loadTexts:vmwObsoleteMIB.setRevisions(('2008-10-15 11:59',))
_VmwCpuTable_Object=MibTable
vmwCpuTable=_VmwCpuTable_Object((1,3,6,1,4,1,6876,3,1,2))
if mibBuilder.loadTexts:vmwCpuTable.setStatus(_B)
_VmwCpuEntry_Object=MibTableRow
vmwCpuEntry=_VmwCpuEntry_Object((1,3,6,1,4,1,6876,3,1,2,1))
vmwCpuEntry.setIndexNames((0,_A,_Q))
if mibBuilder.loadTexts:vmwCpuEntry.setStatus(_B)
class _VmwCpuVMID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_VmwCpuVMID_Type.__name__=_I
_VmwCpuVMID_Object=MibTableColumn
vmwCpuVMID=_VmwCpuVMID_Object((1,3,6,1,4,1,6876,3,1,2,1,1),_VmwCpuVMID_Type())
vmwCpuVMID.setMaxAccess(_J)
if mibBuilder.loadTexts:vmwCpuVMID.setStatus(_E)
_VmwCpuShares_Type=Gauge32
_VmwCpuShares_Object=MibTableColumn
vmwCpuShares=_VmwCpuShares_Object((1,3,6,1,4,1,6876,3,1,2,1,2),_VmwCpuShares_Type())
vmwCpuShares.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwCpuShares.setStatus(_E)
if mibBuilder.loadTexts:vmwCpuShares.setUnits(_R)
_VmwCpuUtil_Type=Gauge32
_VmwCpuUtil_Object=MibTableColumn
vmwCpuUtil=_VmwCpuUtil_Object((1,3,6,1,4,1,6876,3,1,2,1,3),_VmwCpuUtil_Type())
vmwCpuUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwCpuUtil.setStatus(_E)
if mibBuilder.loadTexts:vmwCpuUtil.setUnits('seconds')
_VmwMemTable_Object=MibTable
vmwMemTable=_VmwMemTable_Object((1,3,6,1,4,1,6876,3,2,4))
if mibBuilder.loadTexts:vmwMemTable.setStatus(_B)
_VmwMemEntry_Object=MibTableRow
vmwMemEntry=_VmwMemEntry_Object((1,3,6,1,4,1,6876,3,2,4,1))
vmwMemEntry.setIndexNames((0,_A,_S))
if mibBuilder.loadTexts:vmwMemEntry.setStatus(_B)
class _VmwMemVMID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_VmwMemVMID_Type.__name__=_I
_VmwMemVMID_Object=MibTableColumn
vmwMemVMID=_VmwMemVMID_Object((1,3,6,1,4,1,6876,3,2,4,1,1),_VmwMemVMID_Type())
vmwMemVMID.setMaxAccess(_J)
if mibBuilder.loadTexts:vmwMemVMID.setStatus(_B)
_VmwMemShares_Type=Gauge32
_VmwMemShares_Object=MibTableColumn
vmwMemShares=_VmwMemShares_Object((1,3,6,1,4,1,6876,3,2,4,1,2),_VmwMemShares_Type())
vmwMemShares.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwMemShares.setStatus(_B)
if mibBuilder.loadTexts:vmwMemShares.setUnits(_R)
_VmwMemConfigured_Type=Gauge32
_VmwMemConfigured_Object=MibTableColumn
vmwMemConfigured=_VmwMemConfigured_Object((1,3,6,1,4,1,6876,3,2,4,1,3),_VmwMemConfigured_Type())
vmwMemConfigured.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwMemConfigured.setStatus(_B)
if mibBuilder.loadTexts:vmwMemConfigured.setUnits(_T)
_VmwMemUtil_Type=Gauge32
_VmwMemUtil_Object=MibTableColumn
vmwMemUtil=_VmwMemUtil_Object((1,3,6,1,4,1,6876,3,2,4,1,4),_VmwMemUtil_Type())
vmwMemUtil.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwMemUtil.setStatus(_B)
if mibBuilder.loadTexts:vmwMemUtil.setUnits(_T)
_VmwHBATable_Object=MibTable
vmwHBATable=_VmwHBATable_Object((1,3,6,1,4,1,6876,3,3))
if mibBuilder.loadTexts:vmwHBATable.setStatus(_B)
_VmwHBAEntry_Object=MibTableRow
vmwHBAEntry=_VmwHBAEntry_Object((1,3,6,1,4,1,6876,3,3,1))
vmwHBAEntry.setIndexNames((0,_A,_U))
if mibBuilder.loadTexts:vmwHBAEntry.setStatus(_B)
class _VmwHbaIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_VmwHbaIdx_Type.__name__=_I
_VmwHbaIdx_Object=MibTableColumn
vmwHbaIdx=_VmwHbaIdx_Object((1,3,6,1,4,1,6876,3,3,1,1),_VmwHbaIdx_Type())
vmwHbaIdx.setMaxAccess(_J)
if mibBuilder.loadTexts:vmwHbaIdx.setStatus(_B)
_VmwHbaName_Type=DisplayString
_VmwHbaName_Object=MibTableColumn
vmwHbaName=_VmwHbaName_Object((1,3,6,1,4,1,6876,3,3,1,2),_VmwHbaName_Type())
vmwHbaName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwHbaName.setStatus(_B)
_VmwHbaVMID_Type=Integer32
_VmwHbaVMID_Object=MibTableColumn
vmwHbaVMID=_VmwHbaVMID_Object((1,3,6,1,4,1,6876,3,3,1,3),_VmwHbaVMID_Type())
vmwHbaVMID.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwHbaVMID.setStatus(_B)
_VmwDiskShares_Type=Gauge32
_VmwDiskShares_Object=MibTableColumn
vmwDiskShares=_VmwDiskShares_Object((1,3,6,1,4,1,6876,3,3,1,4),_VmwDiskShares_Type())
vmwDiskShares.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwDiskShares.setStatus(_B)
_VmwNumReads_Type=Counter32
_VmwNumReads_Object=MibTableColumn
vmwNumReads=_VmwNumReads_Object((1,3,6,1,4,1,6876,3,3,1,5),_VmwNumReads_Type())
vmwNumReads.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwNumReads.setStatus(_B)
_VmwKbRead_Type=Counter32
_VmwKbRead_Object=MibTableColumn
vmwKbRead=_VmwKbRead_Object((1,3,6,1,4,1,6876,3,3,1,6),_VmwKbRead_Type())
vmwKbRead.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwKbRead.setStatus(_B)
_VmwNumWrites_Type=Counter32
_VmwNumWrites_Object=MibTableColumn
vmwNumWrites=_VmwNumWrites_Object((1,3,6,1,4,1,6876,3,3,1,7),_VmwNumWrites_Type())
vmwNumWrites.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwNumWrites.setStatus(_B)
_VmwKbWritten_Type=Counter32
_VmwKbWritten_Object=MibTableColumn
vmwKbWritten=_VmwKbWritten_Object((1,3,6,1,4,1,6876,3,3,1,8),_VmwKbWritten_Type())
vmwKbWritten.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwKbWritten.setStatus(_B)
_VmwNetTable_Object=MibTable
vmwNetTable=_VmwNetTable_Object((1,3,6,1,4,1,6876,3,4))
if mibBuilder.loadTexts:vmwNetTable.setStatus(_B)
_VmwNetEntry_Object=MibTableRow
vmwNetEntry=_VmwNetEntry_Object((1,3,6,1,4,1,6876,3,4,1))
vmwNetEntry.setIndexNames((0,_A,_V))
if mibBuilder.loadTexts:vmwNetEntry.setStatus(_B)
class _VmwNetIdx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_VmwNetIdx_Type.__name__=_I
_VmwNetIdx_Object=MibTableColumn
vmwNetIdx=_VmwNetIdx_Object((1,3,6,1,4,1,6876,3,4,1,1),_VmwNetIdx_Type())
vmwNetIdx.setMaxAccess(_J)
if mibBuilder.loadTexts:vmwNetIdx.setStatus(_B)
_VmwNetName_Type=DisplayString
_VmwNetName_Object=MibTableColumn
vmwNetName=_VmwNetName_Object((1,3,6,1,4,1,6876,3,4,1,2),_VmwNetName_Type())
vmwNetName.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwNetName.setStatus(_B)
_VmwNetVMID_Type=Integer32
_VmwNetVMID_Object=MibTableColumn
vmwNetVMID=_VmwNetVMID_Object((1,3,6,1,4,1,6876,3,4,1,3),_VmwNetVMID_Type())
vmwNetVMID.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwNetVMID.setStatus(_B)
_VmwNetIfAddr_Type=DisplayString
_VmwNetIfAddr_Object=MibTableColumn
vmwNetIfAddr=_VmwNetIfAddr_Object((1,3,6,1,4,1,6876,3,4,1,4),_VmwNetIfAddr_Type())
vmwNetIfAddr.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwNetIfAddr.setStatus(_B)
_VmwNetShares_Type=Gauge32
_VmwNetShares_Object=MibTableColumn
vmwNetShares=_VmwNetShares_Object((1,3,6,1,4,1,6876,3,4,1,5),_VmwNetShares_Type())
vmwNetShares.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwNetShares.setStatus(_B)
_VmwNetPktsTx_Type=Counter32
_VmwNetPktsTx_Object=MibTableColumn
vmwNetPktsTx=_VmwNetPktsTx_Object((1,3,6,1,4,1,6876,3,4,1,6),_VmwNetPktsTx_Type())
vmwNetPktsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwNetPktsTx.setStatus(_B)
_VmwNetKbTx_Type=Counter32
_VmwNetKbTx_Object=MibTableColumn
vmwNetKbTx=_VmwNetKbTx_Object((1,3,6,1,4,1,6876,3,4,1,7),_VmwNetKbTx_Type())
vmwNetKbTx.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwNetKbTx.setStatus(_B)
_VmwNetPktsRx_Type=Counter32
_VmwNetPktsRx_Object=MibTableColumn
vmwNetPktsRx=_VmwNetPktsRx_Object((1,3,6,1,4,1,6876,3,4,1,8),_VmwNetPktsRx_Type())
vmwNetPktsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwNetPktsRx.setStatus(_B)
_VmwNetKbRx_Type=Counter32
_VmwNetKbRx_Object=MibTableColumn
vmwNetKbRx=_VmwNetKbRx_Object((1,3,6,1,4,1,6876,3,4,1,9),_VmwNetKbRx_Type())
vmwNetKbRx.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwNetKbRx.setStatus(_B)
_VmwNetHCPktsTx_Type=Counter64
_VmwNetHCPktsTx_Object=MibTableColumn
vmwNetHCPktsTx=_VmwNetHCPktsTx_Object((1,3,6,1,4,1,6876,3,4,1,10),_VmwNetHCPktsTx_Type())
vmwNetHCPktsTx.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwNetHCPktsTx.setStatus(_B)
_VmwNetHCKbTx_Type=Counter64
_VmwNetHCKbTx_Object=MibTableColumn
vmwNetHCKbTx=_VmwNetHCKbTx_Object((1,3,6,1,4,1,6876,3,4,1,11),_VmwNetHCKbTx_Type())
vmwNetHCKbTx.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwNetHCKbTx.setStatus(_B)
_VmwNetHCPktsRx_Type=Counter64
_VmwNetHCPktsRx_Object=MibTableColumn
vmwNetHCPktsRx=_VmwNetHCPktsRx_Object((1,3,6,1,4,1,6876,3,4,1,12),_VmwNetHCPktsRx_Type())
vmwNetHCPktsRx.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwNetHCPktsRx.setStatus(_B)
_VmwNetHCKbRx_Type=Counter64
_VmwNetHCKbRx_Object=MibTableColumn
vmwNetHCKbRx=_VmwNetHCKbRx_Object((1,3,6,1,4,1,6876,3,4,1,13),_VmwNetHCKbRx_Type())
vmwNetHCKbRx.setMaxAccess(_C)
if mibBuilder.loadTexts:vmwNetHCKbRx.setStatus(_B)
_VmkLoaded_Type=DisplayString
_VmkLoaded_Object=MibScalar
vmkLoaded=_VmkLoaded_Object((1,3,6,1,4,1,6876,4,1,1),_VmkLoaded_Type())
vmkLoaded.setMaxAccess(_C)
if mibBuilder.loadTexts:vmkLoaded.setStatus(_B)
_VpxdTrapType_Type=DisplayString
_VpxdTrapType_Object=MibScalar
vpxdTrapType=_VpxdTrapType_Object((1,3,6,1,4,1,6876,50,301),_VpxdTrapType_Type())
vpxdTrapType.setMaxAccess(_H)
if mibBuilder.loadTexts:vpxdTrapType.setStatus(_E)
_VpxdHostName_Type=DisplayString
_VpxdHostName_Object=MibScalar
vpxdHostName=_VpxdHostName_Object((1,3,6,1,4,1,6876,50,302),_VpxdHostName_Type())
vpxdHostName.setMaxAccess(_H)
if mibBuilder.loadTexts:vpxdHostName.setStatus(_E)
_VpxdVMName_Type=DisplayString
_VpxdVMName_Object=MibScalar
vpxdVMName=_VpxdVMName_Object((1,3,6,1,4,1,6876,50,303),_VpxdVMName_Type())
vpxdVMName.setMaxAccess(_H)
if mibBuilder.loadTexts:vpxdVMName.setStatus(_E)
_VpxdOldStatus_Type=DisplayString
_VpxdOldStatus_Object=MibScalar
vpxdOldStatus=_VpxdOldStatus_Object((1,3,6,1,4,1,6876,50,304),_VpxdOldStatus_Type())
vpxdOldStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:vpxdOldStatus.setStatus(_E)
_VpxdNewStatus_Type=DisplayString
_VpxdNewStatus_Object=MibScalar
vpxdNewStatus=_VpxdNewStatus_Object((1,3,6,1,4,1,6876,50,305),_VpxdNewStatus_Type())
vpxdNewStatus.setMaxAccess(_H)
if mibBuilder.loadTexts:vpxdNewStatus.setStatus(_E)
_VpxdObjValue_Type=DisplayString
_VpxdObjValue_Object=MibScalar
vpxdObjValue=_VpxdObjValue_Object((1,3,6,1,4,1,6876,50,306),_VpxdObjValue_Type())
vpxdObjValue.setMaxAccess(_H)
if mibBuilder.loadTexts:vpxdObjValue.setStatus(_E)
_VmwObsoleteMIBConformance_ObjectIdentity=ObjectIdentity
vmwObsoleteMIBConformance=_VmwObsoleteMIBConformance_ObjectIdentity((1,3,6,1,4,1,6876,800,1,2))
_VmwObsoleteMIBCompliances_ObjectIdentity=ObjectIdentity
vmwObsoleteMIBCompliances=_VmwObsoleteMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6876,800,1,2,1))
_VmwObsMIBGroups_ObjectIdentity=ObjectIdentity
vmwObsMIBGroups=_VmwObsMIBGroups_ObjectIdentity((1,3,6,1,4,1,6876,800,1,2,2))
vmwObsoleteGroup=ObjectGroup((1,3,6,1,4,1,6876,800,1,2,2,2))
vmwObsoleteGroup.setObjects(*((_A,_W),(_A,_X),(_A,_Y),(_A,_Z),(_A,_a),(_A,_b),(_A,_c),(_A,_d),(_A,_e),(_A,_f),(_A,_g),(_A,_h),(_A,_i),(_A,_j),(_A,_k),(_A,_l),(_A,_m),(_A,_n),(_A,_o),(_A,_p),(_A,_q),(_A,_r),(_A,_s),(_A,_t),(_A,_u),(_A,_K),(_A,_L),(_A,_M),(_A,_N),(_A,_O),(_A,_P)))
if mibBuilder.loadTexts:vmwObsoleteGroup.setStatus(_B)
vmPoweredOn=NotificationType((1,3,6,1,4,1,6876,0,1))
vmPoweredOn.setObjects(*((_D,_G),(_D,_F)))
if mibBuilder.loadTexts:vmPoweredOn.setStatus(_B)
vmPoweredOff=NotificationType((1,3,6,1,4,1,6876,0,2))
vmPoweredOff.setObjects(*((_D,_G),(_D,_F)))
if mibBuilder.loadTexts:vmPoweredOff.setStatus(_B)
vmHBLost=NotificationType((1,3,6,1,4,1,6876,0,3))
vmHBLost.setObjects(*((_D,_G),(_D,_F)))
if mibBuilder.loadTexts:vmHBLost.setStatus(_B)
vmHBDetected=NotificationType((1,3,6,1,4,1,6876,0,4))
vmHBDetected.setObjects(*((_D,_G),(_D,_F)))
if mibBuilder.loadTexts:vmHBDetected.setStatus(_B)
vmSuspended=NotificationType((1,3,6,1,4,1,6876,0,5))
vmSuspended.setObjects(*((_D,_G),(_D,_F)))
if mibBuilder.loadTexts:vmSuspended.setStatus(_B)
vpxdTrap=NotificationType((1,3,6,1,4,1,6876,0,201))
vpxdTrap.setObjects(*((_A,_K),(_A,_L),(_A,_M),(_A,_O),(_A,_N),(_A,_P)))
if mibBuilder.loadTexts:vpxdTrap.setStatus(_B)
vmwOldVCNotificationGroup=NotificationGroup((1,3,6,1,4,1,6876,800,1,2,2,3))
vmwOldVCNotificationGroup.setObjects(*((_A,_v),(_A,_w),(_A,_x),(_A,_y),(_A,_z),(_A,_A0)))
if mibBuilder.loadTexts:vmwOldVCNotificationGroup.setStatus(_B)
vmwObsoleteObsoleteMIBCompliance=ModuleCompliance((1,3,6,1,4,1,6876,800,1,2,1,3))
vmwObsoleteObsoleteMIBCompliance.setObjects(*((_A,_A1),(_A,_A2)))
if mibBuilder.loadTexts:vmwObsoleteObsoleteMIBCompliance.setStatus(_B)
mibBuilder.exportSymbols(_A,**{_w:vmPoweredOn,_x:vmPoweredOff,_y:vmHBLost,_z:vmHBDetected,_A0:vmSuspended,_v:vpxdTrap,'vmwCpuTable':vmwCpuTable,'vmwCpuEntry':vmwCpuEntry,_Q:vmwCpuVMID,_X:vmwCpuShares,_Y:vmwCpuUtil,'vmwMemTable':vmwMemTable,'vmwMemEntry':vmwMemEntry,_S:vmwMemVMID,_Z:vmwMemShares,_a:vmwMemConfigured,_b:vmwMemUtil,'vmwHBATable':vmwHBATable,'vmwHBAEntry':vmwHBAEntry,_U:vmwHbaIdx,_c:vmwHbaName,_d:vmwHbaVMID,_e:vmwDiskShares,_f:vmwNumReads,_g:vmwKbRead,_h:vmwNumWrites,_i:vmwKbWritten,'vmwNetTable':vmwNetTable,'vmwNetEntry':vmwNetEntry,_V:vmwNetIdx,_j:vmwNetName,_k:vmwNetVMID,_l:vmwNetIfAddr,_m:vmwNetShares,_n:vmwNetPktsTx,_o:vmwNetKbTx,_p:vmwNetPktsRx,_q:vmwNetKbRx,_r:vmwNetHCPktsTx,_s:vmwNetHCKbTx,_t:vmwNetHCPktsRx,_u:vmwNetHCKbRx,_W:vmkLoaded,_K:vpxdTrapType,_L:vpxdHostName,_M:vpxdVMName,_N:vpxdOldStatus,_O:vpxdNewStatus,_P:vpxdObjValue,'vmwObsoleteMIB':vmwObsoleteMIB,'vmwObsoleteMIBConformance':vmwObsoleteMIBConformance,'vmwObsoleteMIBCompliances':vmwObsoleteMIBCompliances,'vmwObsoleteObsoleteMIBCompliance':vmwObsoleteObsoleteMIBCompliance,'vmwObsMIBGroups':vmwObsMIBGroups,_A1:vmwObsoleteGroup,_A2:vmwOldVCNotificationGroup})