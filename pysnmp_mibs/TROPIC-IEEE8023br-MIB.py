_j='ieee8023brGroup'
_i='aMACMergeAcctPolicyId'
_h='aMACMergeHoldCount'
_g='aMACMergeFragCountTx'
_f='aMACMergeFragCountRx'
_e='aMACMergeFrameAssOkCount'
_d='aMACMergeFrameSmdErrorCount'
_c='aMACMergeFrameAssErrorCount'
_b='aMACMergeAddFragSize'
_a='aMACMergeVerifyTime'
_Z='aMACMergeStatusTx'
_Y='aMACMergeVerifyDisableTx'
_X='aMACMergeEnableTx'
_W='aMACMergeStatusVerify'
_V='aMACMergeSupport'
_U='aLldpXdot3RemAddFragSize'
_T='aLldpXdot3RemPreemptActive'
_S='aLldpXdot3RemPreemptEnabled'
_R='aLldpXdot3RemPreemptSupported'
_Q='aLldpXdot3LocAddFragSize'
_P='aLldpXdot3LocPreemptActive'
_O='aLldpXdot3LocPreemptEnabled'
_N='aLldpXdot3LocPreemptSupported'
_M='unknown'
_L='aMACMergePortID'
_K='aLldpXdot3RemPortID'
_J='aLldpXdot3LocPortID'
_I='Unsigned32'
_H='false'
_G='true'
_F='not-accessible'
_E='read-create'
_D='Integer32'
_C='read-only'
_B='TROPIC-IEEE8023br-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
TmnxPortID,=mibBuilder.importSymbols('TN-TC-MIB','TmnxPortID')
tnIEEE8023brMIB,tnPortModules=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnIEEE8023brMIB','tnPortModules')
tnIEEE8023brMibModule=ModuleIdentity((1,3,6,1,4,1,7483,1,1,2,2,4,9))
if mibBuilder.loadTexts:tnIEEE8023brMibModule.setRevisions(('2016-08-15 00:00',))
_TnIEEE8023brEquipmentObjectsNotifications_ObjectIdentity=ObjectIdentity
tnIEEE8023brEquipmentObjectsNotifications=_TnIEEE8023brEquipmentObjectsNotifications_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,11,0))
_TnIEEE8023brObjects_ObjectIdentity=ObjectIdentity
tnIEEE8023brObjects=_TnIEEE8023brObjects_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,11,1))
_TnIEEE8023brObjectsParameters_ObjectIdentity=ObjectIdentity
tnIEEE8023brObjectsParameters=_TnIEEE8023brObjectsParameters_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,11,1,1))
_LldpXdot3LocSystemsGroupTable_Object=MibTable
lldpXdot3LocSystemsGroupTable=_LldpXdot3LocSystemsGroupTable_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,1))
if mibBuilder.loadTexts:lldpXdot3LocSystemsGroupTable.setStatus(_A)
_LldpXdot3LocSystemsGroupEntry_Object=MibTableRow
lldpXdot3LocSystemsGroupEntry=_LldpXdot3LocSystemsGroupEntry_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,1,1))
lldpXdot3LocSystemsGroupEntry.setIndexNames((0,_B,_J))
if mibBuilder.loadTexts:lldpXdot3LocSystemsGroupEntry.setStatus(_A)
_ALldpXdot3LocPortID_Type=TmnxPortID
_ALldpXdot3LocPortID_Object=MibTableColumn
aLldpXdot3LocPortID=_ALldpXdot3LocPortID_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,1,1,1),_ALldpXdot3LocPortID_Type())
aLldpXdot3LocPortID.setMaxAccess(_F)
if mibBuilder.loadTexts:aLldpXdot3LocPortID.setStatus(_A)
_ALldpXdot3LocPreemptSupported_Type=TruthValue
_ALldpXdot3LocPreemptSupported_Object=MibTableColumn
aLldpXdot3LocPreemptSupported=_ALldpXdot3LocPreemptSupported_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,1,1,2),_ALldpXdot3LocPreemptSupported_Type())
aLldpXdot3LocPreemptSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:aLldpXdot3LocPreemptSupported.setStatus(_A)
_ALldpXdot3LocPreemptEnabled_Type=TruthValue
_ALldpXdot3LocPreemptEnabled_Object=MibTableColumn
aLldpXdot3LocPreemptEnabled=_ALldpXdot3LocPreemptEnabled_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,1,1,3),_ALldpXdot3LocPreemptEnabled_Type())
aLldpXdot3LocPreemptEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:aLldpXdot3LocPreemptEnabled.setStatus(_A)
_ALldpXdot3LocPreemptActive_Type=TruthValue
_ALldpXdot3LocPreemptActive_Object=MibTableColumn
aLldpXdot3LocPreemptActive=_ALldpXdot3LocPreemptActive_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,1,1,4),_ALldpXdot3LocPreemptActive_Type())
aLldpXdot3LocPreemptActive.setMaxAccess(_C)
if mibBuilder.loadTexts:aLldpXdot3LocPreemptActive.setStatus(_A)
_ALldpXdot3LocAddFragSize_Type=TruthValue
_ALldpXdot3LocAddFragSize_Object=MibTableColumn
aLldpXdot3LocAddFragSize=_ALldpXdot3LocAddFragSize_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,1,1,5),_ALldpXdot3LocAddFragSize_Type())
aLldpXdot3LocAddFragSize.setMaxAccess(_E)
if mibBuilder.loadTexts:aLldpXdot3LocAddFragSize.setStatus(_A)
_LldpXdot3RemSystemsGroupTable_Object=MibTable
lldpXdot3RemSystemsGroupTable=_LldpXdot3RemSystemsGroupTable_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,2))
if mibBuilder.loadTexts:lldpXdot3RemSystemsGroupTable.setStatus(_A)
_LldpXdot3RemSystemsGroupEntry_Object=MibTableRow
lldpXdot3RemSystemsGroupEntry=_LldpXdot3RemSystemsGroupEntry_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,2,1))
lldpXdot3RemSystemsGroupEntry.setIndexNames((0,_B,_K))
if mibBuilder.loadTexts:lldpXdot3RemSystemsGroupEntry.setStatus(_A)
_ALldpXdot3RemPortID_Type=TmnxPortID
_ALldpXdot3RemPortID_Object=MibTableColumn
aLldpXdot3RemPortID=_ALldpXdot3RemPortID_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,2,1,1),_ALldpXdot3RemPortID_Type())
aLldpXdot3RemPortID.setMaxAccess(_F)
if mibBuilder.loadTexts:aLldpXdot3RemPortID.setStatus(_A)
_ALldpXdot3RemPreemptSupported_Type=TruthValue
_ALldpXdot3RemPreemptSupported_Object=MibTableColumn
aLldpXdot3RemPreemptSupported=_ALldpXdot3RemPreemptSupported_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,2,1,2),_ALldpXdot3RemPreemptSupported_Type())
aLldpXdot3RemPreemptSupported.setMaxAccess(_C)
if mibBuilder.loadTexts:aLldpXdot3RemPreemptSupported.setStatus(_A)
_ALldpXdot3RemPreemptEnabled_Type=TruthValue
_ALldpXdot3RemPreemptEnabled_Object=MibTableColumn
aLldpXdot3RemPreemptEnabled=_ALldpXdot3RemPreemptEnabled_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,2,1,3),_ALldpXdot3RemPreemptEnabled_Type())
aLldpXdot3RemPreemptEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:aLldpXdot3RemPreemptEnabled.setStatus(_A)
_ALldpXdot3RemPreemptActive_Type=TruthValue
_ALldpXdot3RemPreemptActive_Object=MibTableColumn
aLldpXdot3RemPreemptActive=_ALldpXdot3RemPreemptActive_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,2,1,4),_ALldpXdot3RemPreemptActive_Type())
aLldpXdot3RemPreemptActive.setMaxAccess(_C)
if mibBuilder.loadTexts:aLldpXdot3RemPreemptActive.setStatus(_A)
_ALldpXdot3RemAddFragSize_Type=TruthValue
_ALldpXdot3RemAddFragSize_Object=MibTableColumn
aLldpXdot3RemAddFragSize=_ALldpXdot3RemAddFragSize_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,2,1,5),_ALldpXdot3RemAddFragSize_Type())
aLldpXdot3RemAddFragSize.setMaxAccess(_C)
if mibBuilder.loadTexts:aLldpXdot3RemAddFragSize.setStatus(_A)
_MacMergeEntityTable_Object=MibTable
macMergeEntityTable=_MacMergeEntityTable_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,3))
if mibBuilder.loadTexts:macMergeEntityTable.setStatus(_A)
_MacMergeEntityEntry_Object=MibTableRow
macMergeEntityEntry=_MacMergeEntityEntry_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,3,1))
macMergeEntityEntry.setIndexNames((0,_B,_L))
if mibBuilder.loadTexts:macMergeEntityEntry.setStatus(_A)
_AMACMergePortID_Type=TmnxPortID
_AMACMergePortID_Object=MibTableColumn
aMACMergePortID=_AMACMergePortID_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,3,1,1),_AMACMergePortID_Type())
aMACMergePortID.setMaxAccess(_F)
if mibBuilder.loadTexts:aMACMergePortID.setStatus(_A)
class _AMACMergeSupport_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AMACMergeSupport_Type.__name__=_D
_AMACMergeSupport_Object=MibTableColumn
aMACMergeSupport=_AMACMergeSupport_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,3,1,2),_AMACMergeSupport_Type())
aMACMergeSupport.setMaxAccess(_C)
if mibBuilder.loadTexts:aMACMergeSupport.setStatus(_A)
class _AMACMergeStatusVerify_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*((_M,0),('initial',1),('verifying',2),('succeeded',3),('failed',4),('disabled',5)))
_AMACMergeStatusVerify_Type.__name__=_D
_AMACMergeStatusVerify_Object=MibTableColumn
aMACMergeStatusVerify=_AMACMergeStatusVerify_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,3,1,3),_AMACMergeStatusVerify_Type())
aMACMergeStatusVerify.setMaxAccess(_C)
if mibBuilder.loadTexts:aMACMergeStatusVerify.setStatus(_A)
class _AMACMergeEnableTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AMACMergeEnableTx_Type.__name__=_D
_AMACMergeEnableTx_Object=MibTableColumn
aMACMergeEnableTx=_AMACMergeEnableTx_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,3,1,4),_AMACMergeEnableTx_Type())
aMACMergeEnableTx.setMaxAccess(_E)
if mibBuilder.loadTexts:aMACMergeEnableTx.setStatus(_A)
class _AMACMergeVerifyDisableTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_AMACMergeVerifyDisableTx_Type.__name__=_D
_AMACMergeVerifyDisableTx_Object=MibTableColumn
aMACMergeVerifyDisableTx=_AMACMergeVerifyDisableTx_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,3,1,5),_AMACMergeVerifyDisableTx_Type())
aMACMergeVerifyDisableTx.setMaxAccess(_E)
if mibBuilder.loadTexts:aMACMergeVerifyDisableTx.setStatus(_A)
class _AMACMergeStatusTx_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_M,0),('inactive',1),('active',2)))
_AMACMergeStatusTx_Type.__name__=_D
_AMACMergeStatusTx_Object=MibTableColumn
aMACMergeStatusTx=_AMACMergeStatusTx_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,3,1,6),_AMACMergeStatusTx_Type())
aMACMergeStatusTx.setMaxAccess(_C)
if mibBuilder.loadTexts:aMACMergeStatusTx.setStatus(_A)
class _AMACMergeVerifyTime_Type(Integer32):defaultValue=10;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,128))
_AMACMergeVerifyTime_Type.__name__=_D
_AMACMergeVerifyTime_Object=MibTableColumn
aMACMergeVerifyTime=_AMACMergeVerifyTime_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,3,1,7),_AMACMergeVerifyTime_Type())
aMACMergeVerifyTime.setMaxAccess(_E)
if mibBuilder.loadTexts:aMACMergeVerifyTime.setStatus(_A)
class _AMACMergeAddFragSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,3))
_AMACMergeAddFragSize_Type.__name__=_D
_AMACMergeAddFragSize_Object=MibTableColumn
aMACMergeAddFragSize=_AMACMergeAddFragSize_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,3,1,8),_AMACMergeAddFragSize_Type())
aMACMergeAddFragSize.setMaxAccess(_E)
if mibBuilder.loadTexts:aMACMergeAddFragSize.setStatus(_A)
_AMACMergeFrameAssErrorCount_Type=Counter64
_AMACMergeFrameAssErrorCount_Object=MibTableColumn
aMACMergeFrameAssErrorCount=_AMACMergeFrameAssErrorCount_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,3,1,9),_AMACMergeFrameAssErrorCount_Type())
aMACMergeFrameAssErrorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:aMACMergeFrameAssErrorCount.setStatus(_A)
_AMACMergeFrameSmdErrorCount_Type=Counter64
_AMACMergeFrameSmdErrorCount_Object=MibTableColumn
aMACMergeFrameSmdErrorCount=_AMACMergeFrameSmdErrorCount_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,3,1,10),_AMACMergeFrameSmdErrorCount_Type())
aMACMergeFrameSmdErrorCount.setMaxAccess(_C)
if mibBuilder.loadTexts:aMACMergeFrameSmdErrorCount.setStatus(_A)
_AMACMergeFrameAssOkCount_Type=Counter64
_AMACMergeFrameAssOkCount_Object=MibTableColumn
aMACMergeFrameAssOkCount=_AMACMergeFrameAssOkCount_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,3,1,11),_AMACMergeFrameAssOkCount_Type())
aMACMergeFrameAssOkCount.setMaxAccess(_C)
if mibBuilder.loadTexts:aMACMergeFrameAssOkCount.setStatus(_A)
_AMACMergeFragCountRx_Type=Counter64
_AMACMergeFragCountRx_Object=MibTableColumn
aMACMergeFragCountRx=_AMACMergeFragCountRx_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,3,1,12),_AMACMergeFragCountRx_Type())
aMACMergeFragCountRx.setMaxAccess(_C)
if mibBuilder.loadTexts:aMACMergeFragCountRx.setStatus(_A)
_AMACMergeFragCountTx_Type=Counter64
_AMACMergeFragCountTx_Object=MibTableColumn
aMACMergeFragCountTx=_AMACMergeFragCountTx_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,3,1,13),_AMACMergeFragCountTx_Type())
aMACMergeFragCountTx.setMaxAccess(_C)
if mibBuilder.loadTexts:aMACMergeFragCountTx.setStatus(_A)
_AMACMergeHoldCount_Type=Counter64
_AMACMergeHoldCount_Object=MibTableColumn
aMACMergeHoldCount=_AMACMergeHoldCount_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,3,1,14),_AMACMergeHoldCount_Type())
aMACMergeHoldCount.setMaxAccess(_C)
if mibBuilder.loadTexts:aMACMergeHoldCount.setStatus(_A)
class _AMACMergeAcctPolicyId_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,99))
_AMACMergeAcctPolicyId_Type.__name__=_I
_AMACMergeAcctPolicyId_Object=MibTableColumn
aMACMergeAcctPolicyId=_AMACMergeAcctPolicyId_Object((1,3,6,1,4,1,7483,2,2,4,11,1,1,3,1,15),_AMACMergeAcctPolicyId_Type())
aMACMergeAcctPolicyId.setMaxAccess(_E)
if mibBuilder.loadTexts:aMACMergeAcctPolicyId.setStatus(_A)
_TnIEEE8023brObjectsConformance_ObjectIdentity=ObjectIdentity
tnIEEE8023brObjectsConformance=_TnIEEE8023brObjectsConformance_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,11,2))
_Ieee8023brCompliances_ObjectIdentity=ObjectIdentity
ieee8023brCompliances=_Ieee8023brCompliances_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,11,2,1))
_Ieee8023brGroups_ObjectIdentity=ObjectIdentity
ieee8023brGroups=_Ieee8023brGroups_ObjectIdentity((1,3,6,1,4,1,7483,2,2,4,11,2,2))
ieee8023brGroup=ObjectGroup((1,3,6,1,4,1,7483,2,2,4,11,2,2,1))
ieee8023brGroup.setObjects(*((_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i)))
if mibBuilder.loadTexts:ieee8023brGroup.setStatus(_A)
ieee8023brCompliance=ModuleCompliance((1,3,6,1,4,1,7483,2,2,4,11,2,1,1))
ieee8023brCompliance.setObjects((_B,_j))
if mibBuilder.loadTexts:ieee8023brCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tnIEEE8023brMibModule':tnIEEE8023brMibModule,'tnIEEE8023brEquipmentObjectsNotifications':tnIEEE8023brEquipmentObjectsNotifications,'tnIEEE8023brObjects':tnIEEE8023brObjects,'tnIEEE8023brObjectsParameters':tnIEEE8023brObjectsParameters,'lldpXdot3LocSystemsGroupTable':lldpXdot3LocSystemsGroupTable,'lldpXdot3LocSystemsGroupEntry':lldpXdot3LocSystemsGroupEntry,_J:aLldpXdot3LocPortID,_N:aLldpXdot3LocPreemptSupported,_O:aLldpXdot3LocPreemptEnabled,_P:aLldpXdot3LocPreemptActive,_Q:aLldpXdot3LocAddFragSize,'lldpXdot3RemSystemsGroupTable':lldpXdot3RemSystemsGroupTable,'lldpXdot3RemSystemsGroupEntry':lldpXdot3RemSystemsGroupEntry,_K:aLldpXdot3RemPortID,_R:aLldpXdot3RemPreemptSupported,_S:aLldpXdot3RemPreemptEnabled,_T:aLldpXdot3RemPreemptActive,_U:aLldpXdot3RemAddFragSize,'macMergeEntityTable':macMergeEntityTable,'macMergeEntityEntry':macMergeEntityEntry,_L:aMACMergePortID,_V:aMACMergeSupport,_W:aMACMergeStatusVerify,_X:aMACMergeEnableTx,_Y:aMACMergeVerifyDisableTx,_Z:aMACMergeStatusTx,_a:aMACMergeVerifyTime,_b:aMACMergeAddFragSize,_c:aMACMergeFrameAssErrorCount,_d:aMACMergeFrameSmdErrorCount,_e:aMACMergeFrameAssOkCount,_f:aMACMergeFragCountRx,_g:aMACMergeFragCountTx,_h:aMACMergeHoldCount,_i:aMACMergeAcctPolicyId,'tnIEEE8023brObjectsConformance':tnIEEE8023brObjectsConformance,'ieee8023brCompliances':ieee8023brCompliances,'ieee8023brCompliance':ieee8023brCompliance,'ieee8023brGroups':ieee8023brGroups,_j:ieee8023brGroup})