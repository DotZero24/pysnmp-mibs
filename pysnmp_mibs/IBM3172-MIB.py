_l='ibm3172Group'
_k='ibm3172ifDeviceNumber'
_j='ibm3172ifOutDblkDiscards'
_i='ibm3172ifOutDblkErrors'
_h='ibm3172ifDblkXmitFrames'
_g='ibm3172ifDblkRcvBlocks'
_f='ibm3172ifDblkXmitOctets'
_e='ibm3172ifDblkRcvOctets'
_d='ibm3172ifInBlkDiscards'
_c='ibm3172ifInBlkErrors'
_b='ibm3172ifBlkXmitBlocks'
_a='ibm3172ifBlkRcvFrames'
_Z='ibm3172ifBlkXmitOctets'
_Y='ibm3172ifBlkRcvOctets'
_X='ibm3172ifOutLANDiscards'
_W='ibm3172ifInLANDiscards'
_V='ibm3172ifOutLANErrors'
_U='ibm3172ifInLANErrors'
_T='ibm3172ifOutLANFrames'
_S='ibm3172ifInLANFrames'
_R='ibm3172ifOutLANOctets'
_Q='ibm3172ifInLANOctets'
_P='ibm3172ifOutChanBlocks'
_O='ibm3172ifInChanBlocks'
_N='ibm3172ifOutChanOctets'
_M='ibm3172ifInChanOctets'
_L='ibm3172ifTrapEnable'
_K='ibm3172ifNumber'
_J='ibm3172Location'
_I='ibm3172Contact'
_H='ibm3172Descr'
_G='Integer32'
_F='DisplayString'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='IBM3172-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','TextualConvention')
ibm3172MIB=ModuleIdentity((1,3,6,1,4,1,2,6,1,8))
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2))
_IbmProd_ObjectIdentity=ObjectIdentity
ibmProd=_IbmProd_ObjectIdentity((1,3,6,1,4,1,2,6))
_Ibm3172_ObjectIdentity=ObjectIdentity
ibm3172=_Ibm3172_ObjectIdentity((1,3,6,1,4,1,2,6,1))
_Ibm3172SystemTable_Object=MibTable
ibm3172SystemTable=_Ibm3172SystemTable_Object((1,3,6,1,4,1,2,6,1,1))
if mibBuilder.loadTexts:ibm3172SystemTable.setStatus(_A)
_Ibm3172SystemTableEntry_Object=MibTableRow
ibm3172SystemTableEntry=_Ibm3172SystemTableEntry_Object((1,3,6,1,4,1,2,6,1,1,1))
ibm3172SystemTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ibm3172SystemTableEntry.setStatus(_A)
class _Ibm3172Descr_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,253))
_Ibm3172Descr_Type.__name__=_F
_Ibm3172Descr_Object=MibTableColumn
ibm3172Descr=_Ibm3172Descr_Object((1,3,6,1,4,1,2,6,1,1,1,1),_Ibm3172Descr_Type())
ibm3172Descr.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172Descr.setStatus(_A)
class _Ibm3172Contact_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Ibm3172Contact_Type.__name__=_F
_Ibm3172Contact_Object=MibTableColumn
ibm3172Contact=_Ibm3172Contact_Object((1,3,6,1,4,1,2,6,1,1,1,2),_Ibm3172Contact_Type())
ibm3172Contact.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172Contact.setStatus(_A)
class _Ibm3172Location_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_Ibm3172Location_Type.__name__=_F
_Ibm3172Location_Object=MibTableColumn
ibm3172Location=_Ibm3172Location_Object((1,3,6,1,4,1,2,6,1,1,1,3),_Ibm3172Location_Type())
ibm3172Location.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172Location.setStatus(_A)
_Ibm3172ifNumber_Type=Integer32
_Ibm3172ifNumber_Object=MibTableColumn
ibm3172ifNumber=_Ibm3172ifNumber_Object((1,3,6,1,4,1,2,6,1,1,1,4),_Ibm3172ifNumber_Type())
ibm3172ifNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifNumber.setStatus(_A)
_Ibm3172ifTrapTable_Object=MibTable
ibm3172ifTrapTable=_Ibm3172ifTrapTable_Object((1,3,6,1,4,1,2,6,1,2))
if mibBuilder.loadTexts:ibm3172ifTrapTable.setStatus(_A)
_Ibm3172ifTrapTableEntry_Object=MibTableRow
ibm3172ifTrapTableEntry=_Ibm3172ifTrapTableEntry_Object((1,3,6,1,4,1,2,6,1,2,1))
ibm3172ifTrapTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ibm3172ifTrapTableEntry.setStatus(_A)
class _Ibm3172ifTrapEnable_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('disabled',1),('enabled',2)))
_Ibm3172ifTrapEnable_Type.__name__=_G
_Ibm3172ifTrapEnable_Object=MibTableColumn
ibm3172ifTrapEnable=_Ibm3172ifTrapEnable_Object((1,3,6,1,4,1,2,6,1,2,1,1),_Ibm3172ifTrapEnable_Type())
ibm3172ifTrapEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifTrapEnable.setStatus(_A)
_Ibm3172ifChanCountersTable_Object=MibTable
ibm3172ifChanCountersTable=_Ibm3172ifChanCountersTable_Object((1,3,6,1,4,1,2,6,1,3))
if mibBuilder.loadTexts:ibm3172ifChanCountersTable.setStatus(_A)
_Ibm3172ifChanCountersTableEntry_Object=MibTableRow
ibm3172ifChanCountersTableEntry=_Ibm3172ifChanCountersTableEntry_Object((1,3,6,1,4,1,2,6,1,3,1))
ibm3172ifChanCountersTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ibm3172ifChanCountersTableEntry.setStatus(_A)
_Ibm3172ifInChanOctets_Type=Counter32
_Ibm3172ifInChanOctets_Object=MibTableColumn
ibm3172ifInChanOctets=_Ibm3172ifInChanOctets_Object((1,3,6,1,4,1,2,6,1,3,1,1),_Ibm3172ifInChanOctets_Type())
ibm3172ifInChanOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifInChanOctets.setStatus(_A)
_Ibm3172ifOutChanOctets_Type=Counter32
_Ibm3172ifOutChanOctets_Object=MibTableColumn
ibm3172ifOutChanOctets=_Ibm3172ifOutChanOctets_Object((1,3,6,1,4,1,2,6,1,3,1,2),_Ibm3172ifOutChanOctets_Type())
ibm3172ifOutChanOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifOutChanOctets.setStatus(_A)
_Ibm3172ifInChanBlocks_Type=Counter32
_Ibm3172ifInChanBlocks_Object=MibTableColumn
ibm3172ifInChanBlocks=_Ibm3172ifInChanBlocks_Object((1,3,6,1,4,1,2,6,1,3,1,3),_Ibm3172ifInChanBlocks_Type())
ibm3172ifInChanBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifInChanBlocks.setStatus(_A)
_Ibm3172ifOutChanBlocks_Type=Counter32
_Ibm3172ifOutChanBlocks_Object=MibTableColumn
ibm3172ifOutChanBlocks=_Ibm3172ifOutChanBlocks_Object((1,3,6,1,4,1,2,6,1,3,1,4),_Ibm3172ifOutChanBlocks_Type())
ibm3172ifOutChanBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifOutChanBlocks.setStatus(_A)
_Ibm3172ifLANCountersTable_Object=MibTable
ibm3172ifLANCountersTable=_Ibm3172ifLANCountersTable_Object((1,3,6,1,4,1,2,6,1,4))
if mibBuilder.loadTexts:ibm3172ifLANCountersTable.setStatus(_A)
_Ibm3172ifLANCountersTableEntry_Object=MibTableRow
ibm3172ifLANCountersTableEntry=_Ibm3172ifLANCountersTableEntry_Object((1,3,6,1,4,1,2,6,1,4,1))
ibm3172ifLANCountersTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ibm3172ifLANCountersTableEntry.setStatus(_A)
_Ibm3172ifInLANOctets_Type=Counter32
_Ibm3172ifInLANOctets_Object=MibTableColumn
ibm3172ifInLANOctets=_Ibm3172ifInLANOctets_Object((1,3,6,1,4,1,2,6,1,4,1,1),_Ibm3172ifInLANOctets_Type())
ibm3172ifInLANOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifInLANOctets.setStatus(_A)
_Ibm3172ifOutLANOctets_Type=Counter32
_Ibm3172ifOutLANOctets_Object=MibTableColumn
ibm3172ifOutLANOctets=_Ibm3172ifOutLANOctets_Object((1,3,6,1,4,1,2,6,1,4,1,2),_Ibm3172ifOutLANOctets_Type())
ibm3172ifOutLANOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifOutLANOctets.setStatus(_A)
_Ibm3172ifInLANFrames_Type=Counter32
_Ibm3172ifInLANFrames_Object=MibTableColumn
ibm3172ifInLANFrames=_Ibm3172ifInLANFrames_Object((1,3,6,1,4,1,2,6,1,4,1,3),_Ibm3172ifInLANFrames_Type())
ibm3172ifInLANFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifInLANFrames.setStatus(_A)
_Ibm3172ifOutLANFrames_Type=Counter32
_Ibm3172ifOutLANFrames_Object=MibTableColumn
ibm3172ifOutLANFrames=_Ibm3172ifOutLANFrames_Object((1,3,6,1,4,1,2,6,1,4,1,4),_Ibm3172ifOutLANFrames_Type())
ibm3172ifOutLANFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifOutLANFrames.setStatus(_A)
_Ibm3172ifInLANErrors_Type=Counter32
_Ibm3172ifInLANErrors_Object=MibTableColumn
ibm3172ifInLANErrors=_Ibm3172ifInLANErrors_Object((1,3,6,1,4,1,2,6,1,4,1,5),_Ibm3172ifInLANErrors_Type())
ibm3172ifInLANErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifInLANErrors.setStatus(_A)
_Ibm3172ifOutLANErrors_Type=Counter32
_Ibm3172ifOutLANErrors_Object=MibTableColumn
ibm3172ifOutLANErrors=_Ibm3172ifOutLANErrors_Object((1,3,6,1,4,1,2,6,1,4,1,6),_Ibm3172ifOutLANErrors_Type())
ibm3172ifOutLANErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifOutLANErrors.setStatus(_A)
_Ibm3172ifInLANDiscards_Type=Counter32
_Ibm3172ifInLANDiscards_Object=MibTableColumn
ibm3172ifInLANDiscards=_Ibm3172ifInLANDiscards_Object((1,3,6,1,4,1,2,6,1,4,1,7),_Ibm3172ifInLANDiscards_Type())
ibm3172ifInLANDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifInLANDiscards.setStatus(_A)
_Ibm3172ifOutLANDiscards_Type=Counter32
_Ibm3172ifOutLANDiscards_Object=MibTableColumn
ibm3172ifOutLANDiscards=_Ibm3172ifOutLANDiscards_Object((1,3,6,1,4,1,2,6,1,4,1,8),_Ibm3172ifOutLANDiscards_Type())
ibm3172ifOutLANDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifOutLANDiscards.setStatus(_A)
_Ibm3172ifBlkCountersTable_Object=MibTable
ibm3172ifBlkCountersTable=_Ibm3172ifBlkCountersTable_Object((1,3,6,1,4,1,2,6,1,5))
if mibBuilder.loadTexts:ibm3172ifBlkCountersTable.setStatus(_A)
_Ibm3172ifBlkCountersTableEntry_Object=MibTableRow
ibm3172ifBlkCountersTableEntry=_Ibm3172ifBlkCountersTableEntry_Object((1,3,6,1,4,1,2,6,1,5,1))
ibm3172ifBlkCountersTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ibm3172ifBlkCountersTableEntry.setStatus(_A)
_Ibm3172ifBlkRcvOctets_Type=Counter32
_Ibm3172ifBlkRcvOctets_Object=MibTableColumn
ibm3172ifBlkRcvOctets=_Ibm3172ifBlkRcvOctets_Object((1,3,6,1,4,1,2,6,1,5,1,1),_Ibm3172ifBlkRcvOctets_Type())
ibm3172ifBlkRcvOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifBlkRcvOctets.setStatus(_A)
_Ibm3172ifBlkXmitOctets_Type=Counter32
_Ibm3172ifBlkXmitOctets_Object=MibTableColumn
ibm3172ifBlkXmitOctets=_Ibm3172ifBlkXmitOctets_Object((1,3,6,1,4,1,2,6,1,5,1,2),_Ibm3172ifBlkXmitOctets_Type())
ibm3172ifBlkXmitOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifBlkXmitOctets.setStatus(_A)
_Ibm3172ifBlkRcvFrames_Type=Counter32
_Ibm3172ifBlkRcvFrames_Object=MibTableColumn
ibm3172ifBlkRcvFrames=_Ibm3172ifBlkRcvFrames_Object((1,3,6,1,4,1,2,6,1,5,1,3),_Ibm3172ifBlkRcvFrames_Type())
ibm3172ifBlkRcvFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifBlkRcvFrames.setStatus(_A)
_Ibm3172ifBlkXmitBlocks_Type=Counter32
_Ibm3172ifBlkXmitBlocks_Object=MibTableColumn
ibm3172ifBlkXmitBlocks=_Ibm3172ifBlkXmitBlocks_Object((1,3,6,1,4,1,2,6,1,5,1,4),_Ibm3172ifBlkXmitBlocks_Type())
ibm3172ifBlkXmitBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifBlkXmitBlocks.setStatus(_A)
_Ibm3172ifInBlkErrors_Type=Counter32
_Ibm3172ifInBlkErrors_Object=MibTableColumn
ibm3172ifInBlkErrors=_Ibm3172ifInBlkErrors_Object((1,3,6,1,4,1,2,6,1,5,1,5),_Ibm3172ifInBlkErrors_Type())
ibm3172ifInBlkErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifInBlkErrors.setStatus(_A)
_Ibm3172ifInBlkDiscards_Type=Counter32
_Ibm3172ifInBlkDiscards_Object=MibTableColumn
ibm3172ifInBlkDiscards=_Ibm3172ifInBlkDiscards_Object((1,3,6,1,4,1,2,6,1,5,1,6),_Ibm3172ifInBlkDiscards_Type())
ibm3172ifInBlkDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifInBlkDiscards.setStatus(_A)
_Ibm3172ifDblkCountersTable_Object=MibTable
ibm3172ifDblkCountersTable=_Ibm3172ifDblkCountersTable_Object((1,3,6,1,4,1,2,6,1,6))
if mibBuilder.loadTexts:ibm3172ifDblkCountersTable.setStatus(_A)
_Ibm3172ifDblkCountersTableEntry_Object=MibTableRow
ibm3172ifDblkCountersTableEntry=_Ibm3172ifDblkCountersTableEntry_Object((1,3,6,1,4,1,2,6,1,6,1))
ibm3172ifDblkCountersTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ibm3172ifDblkCountersTableEntry.setStatus(_A)
_Ibm3172ifDblkRcvOctets_Type=Counter32
_Ibm3172ifDblkRcvOctets_Object=MibTableColumn
ibm3172ifDblkRcvOctets=_Ibm3172ifDblkRcvOctets_Object((1,3,6,1,4,1,2,6,1,6,1,1),_Ibm3172ifDblkRcvOctets_Type())
ibm3172ifDblkRcvOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifDblkRcvOctets.setStatus(_A)
_Ibm3172ifDblkXmitOctets_Type=Counter32
_Ibm3172ifDblkXmitOctets_Object=MibTableColumn
ibm3172ifDblkXmitOctets=_Ibm3172ifDblkXmitOctets_Object((1,3,6,1,4,1,2,6,1,6,1,2),_Ibm3172ifDblkXmitOctets_Type())
ibm3172ifDblkXmitOctets.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifDblkXmitOctets.setStatus(_A)
_Ibm3172ifDblkRcvBlocks_Type=Counter32
_Ibm3172ifDblkRcvBlocks_Object=MibTableColumn
ibm3172ifDblkRcvBlocks=_Ibm3172ifDblkRcvBlocks_Object((1,3,6,1,4,1,2,6,1,6,1,3),_Ibm3172ifDblkRcvBlocks_Type())
ibm3172ifDblkRcvBlocks.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifDblkRcvBlocks.setStatus(_A)
_Ibm3172ifDblkXmitFrames_Type=Counter32
_Ibm3172ifDblkXmitFrames_Object=MibTableColumn
ibm3172ifDblkXmitFrames=_Ibm3172ifDblkXmitFrames_Object((1,3,6,1,4,1,2,6,1,6,1,4),_Ibm3172ifDblkXmitFrames_Type())
ibm3172ifDblkXmitFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifDblkXmitFrames.setStatus(_A)
_Ibm3172ifOutDblkErrors_Type=Counter32
_Ibm3172ifOutDblkErrors_Object=MibTableColumn
ibm3172ifOutDblkErrors=_Ibm3172ifOutDblkErrors_Object((1,3,6,1,4,1,2,6,1,6,1,5),_Ibm3172ifOutDblkErrors_Type())
ibm3172ifOutDblkErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifOutDblkErrors.setStatus(_A)
_Ibm3172ifOutDblkDiscards_Type=Counter32
_Ibm3172ifOutDblkDiscards_Object=MibTableColumn
ibm3172ifOutDblkDiscards=_Ibm3172ifOutDblkDiscards_Object((1,3,6,1,4,1,2,6,1,6,1,6),_Ibm3172ifOutDblkDiscards_Type())
ibm3172ifOutDblkDiscards.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifOutDblkDiscards.setStatus(_A)
_Ibm3172ifDeviceTable_Object=MibTable
ibm3172ifDeviceTable=_Ibm3172ifDeviceTable_Object((1,3,6,1,4,1,2,6,1,7))
if mibBuilder.loadTexts:ibm3172ifDeviceTable.setStatus(_A)
_Ibm3172ifDeviceTableEntry_Object=MibTableRow
ibm3172ifDeviceTableEntry=_Ibm3172ifDeviceTableEntry_Object((1,3,6,1,4,1,2,6,1,7,1))
ibm3172ifDeviceTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:ibm3172ifDeviceTableEntry.setStatus(_A)
_Ibm3172ifDeviceNumber_Type=Integer32
_Ibm3172ifDeviceNumber_Object=MibTableColumn
ibm3172ifDeviceNumber=_Ibm3172ifDeviceNumber_Object((1,3,6,1,4,1,2,6,1,7,1,1),_Ibm3172ifDeviceNumber_Type())
ibm3172ifDeviceNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:ibm3172ifDeviceNumber.setStatus(_A)
_Ibm3172MIBConformance_ObjectIdentity=ObjectIdentity
ibm3172MIBConformance=_Ibm3172MIBConformance_ObjectIdentity((1,3,6,1,4,1,2,6,1,8,2))
_Ibm3172MIBCompliances_ObjectIdentity=ObjectIdentity
ibm3172MIBCompliances=_Ibm3172MIBCompliances_ObjectIdentity((1,3,6,1,4,1,2,6,1,8,2,1))
_Ibm3172MIBGroups_ObjectIdentity=ObjectIdentity
ibm3172MIBGroups=_Ibm3172MIBGroups_ObjectIdentity((1,3,6,1,4,1,2,6,1,8,2,2))
ibm3172Group=ObjectGroup((1,3,6,1,4,1,2,6,1,8,2,2,1))
ibm3172Group.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b),(_B,_c),(_B,_d),(_B,_e),(_B,_f),(_B,_g),(_B,_h),(_B,_i),(_B,_j),(_B,_k)))
if mibBuilder.loadTexts:ibm3172Group.setStatus(_A)
ibm3172MIBCompliance=ModuleCompliance((1,3,6,1,4,1,2,6,1,8,2,1,1))
ibm3172MIBCompliance.setObjects((_B,_l))
if mibBuilder.loadTexts:ibm3172MIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ibm':ibm,'ibmProd':ibmProd,'ibm3172':ibm3172,'ibm3172SystemTable':ibm3172SystemTable,'ibm3172SystemTableEntry':ibm3172SystemTableEntry,_H:ibm3172Descr,_I:ibm3172Contact,_J:ibm3172Location,_K:ibm3172ifNumber,'ibm3172ifTrapTable':ibm3172ifTrapTable,'ibm3172ifTrapTableEntry':ibm3172ifTrapTableEntry,_L:ibm3172ifTrapEnable,'ibm3172ifChanCountersTable':ibm3172ifChanCountersTable,'ibm3172ifChanCountersTableEntry':ibm3172ifChanCountersTableEntry,_M:ibm3172ifInChanOctets,_N:ibm3172ifOutChanOctets,_O:ibm3172ifInChanBlocks,_P:ibm3172ifOutChanBlocks,'ibm3172ifLANCountersTable':ibm3172ifLANCountersTable,'ibm3172ifLANCountersTableEntry':ibm3172ifLANCountersTableEntry,_Q:ibm3172ifInLANOctets,_R:ibm3172ifOutLANOctets,_S:ibm3172ifInLANFrames,_T:ibm3172ifOutLANFrames,_U:ibm3172ifInLANErrors,_V:ibm3172ifOutLANErrors,_W:ibm3172ifInLANDiscards,_X:ibm3172ifOutLANDiscards,'ibm3172ifBlkCountersTable':ibm3172ifBlkCountersTable,'ibm3172ifBlkCountersTableEntry':ibm3172ifBlkCountersTableEntry,_Y:ibm3172ifBlkRcvOctets,_Z:ibm3172ifBlkXmitOctets,_a:ibm3172ifBlkRcvFrames,_b:ibm3172ifBlkXmitBlocks,_c:ibm3172ifInBlkErrors,_d:ibm3172ifInBlkDiscards,'ibm3172ifDblkCountersTable':ibm3172ifDblkCountersTable,'ibm3172ifDblkCountersTableEntry':ibm3172ifDblkCountersTableEntry,_e:ibm3172ifDblkRcvOctets,_f:ibm3172ifDblkXmitOctets,_g:ibm3172ifDblkRcvBlocks,_h:ibm3172ifDblkXmitFrames,_i:ibm3172ifOutDblkErrors,_j:ibm3172ifOutDblkDiscards,'ibm3172ifDeviceTable':ibm3172ifDeviceTable,'ibm3172ifDeviceTableEntry':ibm3172ifDeviceTableEntry,_k:ibm3172ifDeviceNumber,'ibm3172MIB':ibm3172MIB,'ibm3172MIBConformance':ibm3172MIBConformance,'ibm3172MIBCompliances':ibm3172MIBCompliances,'ibm3172MIBCompliance':ibm3172MIBCompliance,'ibm3172MIBGroups':ibm3172MIBGroups,_l:ibm3172Group})