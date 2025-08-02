_N='vpxdObjValue'
_M='vpxdOldStatus'
_L='vpxdNewStatus'
_K='vpxdVMName'
_J='vpxdHostName'
_I='vpxdTrapType'
_H='NotificationType'
_G='vmConfigFile'
_F='vmID'
_E='vmwVmDisplayName'
_D='VMWARE-VMINFO-MIB'
_C='mandatory'
_B='read-only'
_A='VMWARE-TRAPS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_H,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_H,'TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
vmwTraps,vmware=mibBuilder.importSymbols('VMWARE-ROOT-MIB','vmwTraps','vmware')
vmwVmDisplayName,=mibBuilder.importSymbols(_D,_E)
_VmID_Type=Integer32
_VmID_Object=MibScalar
vmID=_VmID_Object((1,3,6,1,4,1,6876,50,101),_VmID_Type())
vmID.setMaxAccess(_B)
if mibBuilder.loadTexts:vmID.setStatus(_C)
_VmConfigFile_Type=DisplayString
_VmConfigFile_Object=MibScalar
vmConfigFile=_VmConfigFile_Object((1,3,6,1,4,1,6876,50,102),_VmConfigFile_Type())
vmConfigFile.setMaxAccess(_B)
if mibBuilder.loadTexts:vmConfigFile.setStatus(_C)
_VpxdTrapType_Type=DisplayString
_VpxdTrapType_Object=MibScalar
vpxdTrapType=_VpxdTrapType_Object((1,3,6,1,4,1,6876,50,301),_VpxdTrapType_Type())
vpxdTrapType.setMaxAccess(_B)
if mibBuilder.loadTexts:vpxdTrapType.setStatus(_C)
_VpxdHostName_Type=DisplayString
_VpxdHostName_Object=MibScalar
vpxdHostName=_VpxdHostName_Object((1,3,6,1,4,1,6876,50,302),_VpxdHostName_Type())
vpxdHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:vpxdHostName.setStatus(_C)
_VpxdVMName_Type=DisplayString
_VpxdVMName_Object=MibScalar
vpxdVMName=_VpxdVMName_Object((1,3,6,1,4,1,6876,50,303),_VpxdVMName_Type())
vpxdVMName.setMaxAccess(_B)
if mibBuilder.loadTexts:vpxdVMName.setStatus(_C)
_VpxdOldStatus_Type=DisplayString
_VpxdOldStatus_Object=MibScalar
vpxdOldStatus=_VpxdOldStatus_Object((1,3,6,1,4,1,6876,50,304),_VpxdOldStatus_Type())
vpxdOldStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vpxdOldStatus.setStatus(_C)
_VpxdNewStatus_Type=DisplayString
_VpxdNewStatus_Object=MibScalar
vpxdNewStatus=_VpxdNewStatus_Object((1,3,6,1,4,1,6876,50,305),_VpxdNewStatus_Type())
vpxdNewStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:vpxdNewStatus.setStatus(_C)
_VpxdObjValue_Type=DisplayString
_VpxdObjValue_Object=MibScalar
vpxdObjValue=_VpxdObjValue_Object((1,3,6,1,4,1,6876,50,306),_VpxdObjValue_Type())
vpxdObjValue.setMaxAccess(_B)
if mibBuilder.loadTexts:vpxdObjValue.setStatus(_C)
vmPoweredOn=NotificationType((1,3,6,1,4,1,6876,0,1))
vmPoweredOn.setObjects(*((_A,_F),(_A,_G),(_D,_E)))
if mibBuilder.loadTexts:vmPoweredOn.setStatus('')
vmPoweredOff=NotificationType((1,3,6,1,4,1,6876,0,2))
vmPoweredOff.setObjects(*((_A,_F),(_A,_G),(_D,_E)))
if mibBuilder.loadTexts:vmPoweredOff.setStatus('')
vmHBLost=NotificationType((1,3,6,1,4,1,6876,0,3))
vmHBLost.setObjects(*((_A,_F),(_A,_G),(_D,_E)))
if mibBuilder.loadTexts:vmHBLost.setStatus('')
vmHBDetected=NotificationType((1,3,6,1,4,1,6876,0,4))
vmHBDetected.setObjects(*((_A,_F),(_A,_G),(_D,_E)))
if mibBuilder.loadTexts:vmHBDetected.setStatus('')
vmSuspended=NotificationType((1,3,6,1,4,1,6876,0,5))
vmSuspended.setObjects(*((_A,_F),(_A,_G),(_D,_E)))
if mibBuilder.loadTexts:vmSuspended.setStatus('')
vpxdTrap=NotificationType((1,3,6,1,4,1,6876,50,0,201))
vpxdTrap.setObjects(*((_A,_I),(_A,_J),(_A,_K),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:vpxdTrap.setStatus('')
mibBuilder.exportSymbols(_A,**{'vmPoweredOn':vmPoweredOn,'vmPoweredOff':vmPoweredOff,'vmHBLost':vmHBLost,'vmHBDetected':vmHBDetected,'vmSuspended':vmSuspended,'vpxdTrap':vpxdTrap,_F:vmID,_G:vmConfigFile,_I:vpxdTrapType,_J:vpxdHostName,_K:vpxdVMName,_M:vpxdOldStatus,_L:vpxdNewStatus,_N:vpxdObjValue})