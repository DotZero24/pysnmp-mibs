_S='rmepGroup'
_R='rmepSenderIDTLV'
_Q='rmepInterfaceStatusTLV'
_P='rmepPortStatusTLV'
_O='rmepRDI'
_N='rmepMacAddress'
_M='rmepFailedOkTime'
_L='rmepRmepState'
_K='rmepMDLevel'
_J='rmepRMepType'
_I='rmepRMepId'
_H='rmepLocalMepId'
_G='rmepLocalMepAid'
_F='read-write'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-TP-PXMRMEP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnInterfaceStatusTLV,InfnIsEnabled,InfnPortStatusTLV,InfnRMepType,InfnRmepState,InfnSenderIDTLV=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnInterfaceStatusTLV','InfnIsEnabled','InfnPortStatusTLV','InfnRMepType','InfnRmepState','InfnSenderIDTLV')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rmepMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,77))
_RmepTable_Object=MibTable
rmepTable=_RmepTable_Object((1,3,6,1,4,1,21296,2,2,2,2,77,1))
if mibBuilder.loadTexts:rmepTable.setStatus(_A)
_RmepEntry_Object=MibTableRow
rmepEntry=_RmepEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,77,1,1))
rmepEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rmepEntry.setStatus(_A)
_RmepLocalMepAid_Type=DisplayString
_RmepLocalMepAid_Object=MibTableColumn
rmepLocalMepAid=_RmepLocalMepAid_Object((1,3,6,1,4,1,21296,2,2,2,2,77,1,1,1),_RmepLocalMepAid_Type())
rmepLocalMepAid.setMaxAccess(_C)
if mibBuilder.loadTexts:rmepLocalMepAid.setStatus(_A)
_RmepLocalMepId_Type=Integer32
_RmepLocalMepId_Object=MibTableColumn
rmepLocalMepId=_RmepLocalMepId_Object((1,3,6,1,4,1,21296,2,2,2,2,77,1,1,2),_RmepLocalMepId_Type())
rmepLocalMepId.setMaxAccess(_C)
if mibBuilder.loadTexts:rmepLocalMepId.setStatus(_A)
_RmepRMepId_Type=Integer32
_RmepRMepId_Object=MibTableColumn
rmepRMepId=_RmepRMepId_Object((1,3,6,1,4,1,21296,2,2,2,2,77,1,1,3),_RmepRMepId_Type())
rmepRMepId.setMaxAccess(_C)
if mibBuilder.loadTexts:rmepRMepId.setStatus(_A)
_RmepRMepType_Type=InfnRMepType
_RmepRMepType_Object=MibTableColumn
rmepRMepType=_RmepRMepType_Object((1,3,6,1,4,1,21296,2,2,2,2,77,1,1,4),_RmepRMepType_Type())
rmepRMepType.setMaxAccess(_F)
if mibBuilder.loadTexts:rmepRMepType.setStatus(_A)
_RmepMDLevel_Type=Integer32
_RmepMDLevel_Object=MibTableColumn
rmepMDLevel=_RmepMDLevel_Object((1,3,6,1,4,1,21296,2,2,2,2,77,1,1,5),_RmepMDLevel_Type())
rmepMDLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:rmepMDLevel.setStatus(_A)
_RmepRmepState_Type=InfnRmepState
_RmepRmepState_Object=MibTableColumn
rmepRmepState=_RmepRmepState_Object((1,3,6,1,4,1,21296,2,2,2,2,77,1,1,6),_RmepRmepState_Type())
rmepRmepState.setMaxAccess(_C)
if mibBuilder.loadTexts:rmepRmepState.setStatus(_A)
_RmepFailedOkTime_Type=Integer32
_RmepFailedOkTime_Object=MibTableColumn
rmepFailedOkTime=_RmepFailedOkTime_Object((1,3,6,1,4,1,21296,2,2,2,2,77,1,1,7),_RmepFailedOkTime_Type())
rmepFailedOkTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rmepFailedOkTime.setStatus(_A)
_RmepMacAddress_Type=DisplayString
_RmepMacAddress_Object=MibTableColumn
rmepMacAddress=_RmepMacAddress_Object((1,3,6,1,4,1,21296,2,2,2,2,77,1,1,8),_RmepMacAddress_Type())
rmepMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rmepMacAddress.setStatus(_A)
_RmepRDI_Type=InfnIsEnabled
_RmepRDI_Object=MibTableColumn
rmepRDI=_RmepRDI_Object((1,3,6,1,4,1,21296,2,2,2,2,77,1,1,9),_RmepRDI_Type())
rmepRDI.setMaxAccess(_C)
if mibBuilder.loadTexts:rmepRDI.setStatus(_A)
_RmepPortStatusTLV_Type=InfnPortStatusTLV
_RmepPortStatusTLV_Object=MibTableColumn
rmepPortStatusTLV=_RmepPortStatusTLV_Object((1,3,6,1,4,1,21296,2,2,2,2,77,1,1,10),_RmepPortStatusTLV_Type())
rmepPortStatusTLV.setMaxAccess(_C)
if mibBuilder.loadTexts:rmepPortStatusTLV.setStatus(_A)
_RmepInterfaceStatusTLV_Type=InfnInterfaceStatusTLV
_RmepInterfaceStatusTLV_Object=MibTableColumn
rmepInterfaceStatusTLV=_RmepInterfaceStatusTLV_Object((1,3,6,1,4,1,21296,2,2,2,2,77,1,1,11),_RmepInterfaceStatusTLV_Type())
rmepInterfaceStatusTLV.setMaxAccess(_C)
if mibBuilder.loadTexts:rmepInterfaceStatusTLV.setStatus(_A)
_RmepSenderIDTLV_Type=InfnSenderIDTLV
_RmepSenderIDTLV_Object=MibTableColumn
rmepSenderIDTLV=_RmepSenderIDTLV_Object((1,3,6,1,4,1,21296,2,2,2,2,77,1,1,12),_RmepSenderIDTLV_Type())
rmepSenderIDTLV.setMaxAccess(_F)
if mibBuilder.loadTexts:rmepSenderIDTLV.setStatus(_A)
_RmepConformance_ObjectIdentity=ObjectIdentity
rmepConformance=_RmepConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,77,3))
_RmepCompliances_ObjectIdentity=ObjectIdentity
rmepCompliances=_RmepCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,77,3,1))
_RmepGroups_ObjectIdentity=ObjectIdentity
rmepGroups=_RmepGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,77,3,2))
rmepGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,77,3,2,1))
rmepGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R)))
if mibBuilder.loadTexts:rmepGroup.setStatus(_A)
rmepCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,77,3,1,1))
rmepCompliance.setObjects((_B,_S))
if mibBuilder.loadTexts:rmepCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rmepMIB':rmepMIB,'rmepTable':rmepTable,'rmepEntry':rmepEntry,_G:rmepLocalMepAid,_H:rmepLocalMepId,_I:rmepRMepId,_J:rmepRMepType,_K:rmepMDLevel,_L:rmepRmepState,_M:rmepFailedOkTime,_N:rmepMacAddress,_O:rmepRDI,_P:rmepPortStatusTLV,_Q:rmepInterfaceStatusTLV,_R:rmepSenderIDTLV,'rmepConformance':rmepConformance,'rmepCompliances':rmepCompliances,'rmepCompliance':rmepCompliance,'rmepGroups':rmepGroups,_S:rmepGroup})