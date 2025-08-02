_a='ctFddiFPIM'
_Z='ctFddiFPIMSlotID'
_Y='bypass'
_X='insertFNB1FNB2'
_W='insertFNB2'
_V='insertFNB1'
_U='ctFDDISerialSlotID'
_T='ctFDDIMuxMasterPortID'
_S='ctFDDIMuxMasterPortSlotID'
_R='ctFDDIMuxOutID'
_Q='ctFDDIMuxOutSlot'
_P='ctFDDIMuxEnableSlot'
_O='ctFDDIMuxConfig'
_N='ctFDDIMuxSlot'
_M='ctFDDINMInterSlot'
_L='ctFDDINMConnectionID'
_K='ctFDDINMConnectionSlot'
_J='ctFDDINMEnableSlot'
_I='ctFDDINMConfigID'
_H='ctFDDINMSlot'
_G='ctFDDIResourceID'
_F='ctFDDIResourceSlotID'
_E='read-write'
_D='Integer32'
_C='CTRON-FDDI-FNB-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ctFDDIFnb,=mibBuilder.importSymbols('CTRON-MIB-NAMES','ctFDDIFnb')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CtFDDIResource_ObjectIdentity=ObjectIdentity
ctFDDIResource=_CtFDDIResource_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,5,1,1))
_CtFDDIResourceTable_Object=MibTable
ctFDDIResourceTable=_CtFDDIResourceTable_Object((1,3,6,1,4,1,52,4,1,2,5,1,1,1))
if mibBuilder.loadTexts:ctFDDIResourceTable.setStatus(_A)
_CtFDDIResourceEntry_Object=MibTableRow
ctFDDIResourceEntry=_CtFDDIResourceEntry_Object((1,3,6,1,4,1,52,4,1,2,5,1,1,1,1))
ctFDDIResourceEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:ctFDDIResourceEntry.setStatus(_A)
class _CtFDDIResourceSlotID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CtFDDIResourceSlotID_Type.__name__=_D
_CtFDDIResourceSlotID_Object=MibTableColumn
ctFDDIResourceSlotID=_CtFDDIResourceSlotID_Object((1,3,6,1,4,1,52,4,1,2,5,1,1,1,1,1),_CtFDDIResourceSlotID_Type())
ctFDDIResourceSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIResourceSlotID.setStatus(_A)
_CtFDDIResourceID_Type=Integer32
_CtFDDIResourceID_Object=MibTableColumn
ctFDDIResourceID=_CtFDDIResourceID_Object((1,3,6,1,4,1,52,4,1,2,5,1,1,1,1,2),_CtFDDIResourceID_Type())
ctFDDIResourceID.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIResourceID.setStatus(_A)
_CtFDDIResourceType_Type=ObjectIdentifier
_CtFDDIResourceType_Object=MibTableColumn
ctFDDIResourceType=_CtFDDIResourceType_Object((1,3,6,1,4,1,52,4,1,2,5,1,1,1,1,3),_CtFDDIResourceType_Type())
ctFDDIResourceType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIResourceType.setStatus(_A)
_CtFDDIResourceNumbInstance_Type=Integer32
_CtFDDIResourceNumbInstance_Object=MibTableColumn
ctFDDIResourceNumbInstance=_CtFDDIResourceNumbInstance_Object((1,3,6,1,4,1,52,4,1,2,5,1,1,1,1,4),_CtFDDIResourceNumbInstance_Type())
ctFDDIResourceNumbInstance.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIResourceNumbInstance.setStatus(_A)
_CtFDDINonMux_ObjectIdentity=ObjectIdentity
ctFDDINonMux=_CtFDDINonMux_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,5,1,2))
_CtFDDINonMuxCapTable_Object=MibTable
ctFDDINonMuxCapTable=_CtFDDINonMuxCapTable_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,1))
if mibBuilder.loadTexts:ctFDDINonMuxCapTable.setStatus(_A)
_CtFDDINonMuxCapEntry_Object=MibTableRow
ctFDDINonMuxCapEntry=_CtFDDINonMuxCapEntry_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,1,1))
ctFDDINonMuxCapEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:ctFDDINonMuxCapEntry.setStatus(_A)
class _CtFDDINMSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_CtFDDINMSlot_Type.__name__=_D
_CtFDDINMSlot_Object=MibTableColumn
ctFDDINMSlot=_CtFDDINMSlot_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,1,1,1),_CtFDDINMSlot_Type())
ctFDDINMSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDINMSlot.setStatus(_A)
_CtFDDINMConfigID_Type=Integer32
_CtFDDINMConfigID_Object=MibTableColumn
ctFDDINMConfigID=_CtFDDINMConfigID_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,1,1,2),_CtFDDINMConfigID_Type())
ctFDDINMConfigID.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDINMConfigID.setStatus(_A)
_CtFDDINMConfig_Type=DisplayString
_CtFDDINMConfig_Object=MibTableColumn
ctFDDINMConfig=_CtFDDINMConfig_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,1,1,3),_CtFDDINMConfig_Type())
ctFDDINMConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDINMConfig.setStatus(_A)
_CtFDDINMConfigDesc_Type=DisplayString
_CtFDDINMConfigDesc_Object=MibTableColumn
ctFDDINMConfigDesc=_CtFDDINMConfigDesc_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,1,1,4),_CtFDDINMConfigDesc_Type())
ctFDDINMConfigDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDINMConfigDesc.setStatus(_A)
_CtFDDINonMuxCapEnableTable_Object=MibTable
ctFDDINonMuxCapEnableTable=_CtFDDINonMuxCapEnableTable_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,2))
if mibBuilder.loadTexts:ctFDDINonMuxCapEnableTable.setStatus(_A)
_CtFDDINonMuxCapEnableEntry_Object=MibTableRow
ctFDDINonMuxCapEnableEntry=_CtFDDINonMuxCapEnableEntry_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,2,1))
ctFDDINonMuxCapEnableEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:ctFDDINonMuxCapEnableEntry.setStatus(_A)
_CtFDDINMEnableSlot_Type=Integer32
_CtFDDINMEnableSlot_Object=MibTableColumn
ctFDDINMEnableSlot=_CtFDDINMEnableSlot_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,2,1,1),_CtFDDINMEnableSlot_Type())
ctFDDINMEnableSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDINMEnableSlot.setStatus(_A)
_CtFDDINMCapEnable_Type=Integer32
_CtFDDINMCapEnable_Object=MibTableColumn
ctFDDINMCapEnable=_CtFDDINMCapEnable_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,2,1,2),_CtFDDINMCapEnable_Type())
ctFDDINMCapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ctFDDINMCapEnable.setStatus(_A)
_CtFDDINonMuxConnectionTable_Object=MibTable
ctFDDINonMuxConnectionTable=_CtFDDINonMuxConnectionTable_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,3))
if mibBuilder.loadTexts:ctFDDINonMuxConnectionTable.setStatus(_A)
_CtFDDINonMuxConnectionEntry_Object=MibTableRow
ctFDDINonMuxConnectionEntry=_CtFDDINonMuxConnectionEntry_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,3,1))
ctFDDINonMuxConnectionEntry.setIndexNames((0,_C,_K),(0,_C,_L))
if mibBuilder.loadTexts:ctFDDINonMuxConnectionEntry.setStatus(_A)
_CtFDDINMConnectionSlot_Type=Integer32
_CtFDDINMConnectionSlot_Object=MibTableColumn
ctFDDINMConnectionSlot=_CtFDDINMConnectionSlot_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,3,1,1),_CtFDDINMConnectionSlot_Type())
ctFDDINMConnectionSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDINMConnectionSlot.setStatus(_A)
_CtFDDINMConnectionID_Type=Integer32
_CtFDDINMConnectionID_Object=MibTableColumn
ctFDDINMConnectionID=_CtFDDINMConnectionID_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,3,1,2),_CtFDDINMConnectionID_Type())
ctFDDINMConnectionID.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDINMConnectionID.setStatus(_A)
_CtFDDINMSMT_Type=Integer32
_CtFDDINMSMT_Object=MibTableColumn
ctFDDINMSMT=_CtFDDINMSMT_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,3,1,3),_CtFDDINMSMT_Type())
ctFDDINMSMT.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDINMSMT.setStatus(_A)
_CtFDDINMMAC_Type=Integer32
_CtFDDINMMAC_Object=MibTableColumn
ctFDDINMMAC=_CtFDDINMMAC_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,3,1,4),_CtFDDINMMAC_Type())
ctFDDINMMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDINMMAC.setStatus(_A)
_CtFDDINMBytes_Type=Integer32
_CtFDDINMBytes_Object=MibTableColumn
ctFDDINMBytes=_CtFDDINMBytes_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,3,1,5),_CtFDDINMBytes_Type())
ctFDDINMBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDINMBytes.setStatus(_A)
_CtFDDINMFrames_Type=Integer32
_CtFDDINMFrames_Object=MibTableColumn
ctFDDINMFrames=_CtFDDINMFrames_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,3,1,6),_CtFDDINMFrames_Type())
ctFDDINMFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDINMFrames.setStatus(_A)
_CtFDDINonMuxInterfaceTable_Object=MibTable
ctFDDINonMuxInterfaceTable=_CtFDDINonMuxInterfaceTable_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,4))
if mibBuilder.loadTexts:ctFDDINonMuxInterfaceTable.setStatus(_A)
_CtFDDINonMuxInterfaceEntry_Object=MibTableRow
ctFDDINonMuxInterfaceEntry=_CtFDDINonMuxInterfaceEntry_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,4,1))
ctFDDINonMuxInterfaceEntry.setIndexNames((0,_C,_M))
if mibBuilder.loadTexts:ctFDDINonMuxInterfaceEntry.setStatus(_A)
_CtFDDINMInterSlot_Type=Integer32
_CtFDDINMInterSlot_Object=MibTableColumn
ctFDDINMInterSlot=_CtFDDINMInterSlot_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,4,1,1),_CtFDDINMInterSlot_Type())
ctFDDINMInterSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDINMInterSlot.setStatus(_A)
_CtFDDINMNumbInterfaces_Type=Integer32
_CtFDDINMNumbInterfaces_Object=MibTableColumn
ctFDDINMNumbInterfaces=_CtFDDINMNumbInterfaces_Object((1,3,6,1,4,1,52,4,1,2,5,1,2,4,1,2),_CtFDDINMNumbInterfaces_Type())
ctFDDINMNumbInterfaces.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDINMNumbInterfaces.setStatus(_A)
_CtFDDIMux_ObjectIdentity=ObjectIdentity
ctFDDIMux=_CtFDDIMux_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,5,1,3))
_CtFDDIMuxCapTable_Object=MibTable
ctFDDIMuxCapTable=_CtFDDIMuxCapTable_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,1))
if mibBuilder.loadTexts:ctFDDIMuxCapTable.setStatus(_A)
_CtFDDIMuxCapEntry_Object=MibTableRow
ctFDDIMuxCapEntry=_CtFDDIMuxCapEntry_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,1,1))
ctFDDIMuxCapEntry.setIndexNames((0,_C,_N),(0,_C,_O))
if mibBuilder.loadTexts:ctFDDIMuxCapEntry.setStatus(_A)
class _CtFDDIMuxSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_CtFDDIMuxSlot_Type.__name__=_D
_CtFDDIMuxSlot_Object=MibTableColumn
ctFDDIMuxSlot=_CtFDDIMuxSlot_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,1,1,1),_CtFDDIMuxSlot_Type())
ctFDDIMuxSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIMuxSlot.setStatus(_A)
_CtFDDIMuxConfigID_Type=Integer32
_CtFDDIMuxConfigID_Object=MibTableColumn
ctFDDIMuxConfigID=_CtFDDIMuxConfigID_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,1,1,2),_CtFDDIMuxConfigID_Type())
ctFDDIMuxConfigID.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIMuxConfigID.setStatus(_A)
_CtFDDIMuxConfig_Type=DisplayString
_CtFDDIMuxConfig_Object=MibTableColumn
ctFDDIMuxConfig=_CtFDDIMuxConfig_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,1,1,3),_CtFDDIMuxConfig_Type())
ctFDDIMuxConfig.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIMuxConfig.setStatus(_A)
_CtFDDIMuxConfigDesc_Type=DisplayString
_CtFDDIMuxConfigDesc_Object=MibTableColumn
ctFDDIMuxConfigDesc=_CtFDDIMuxConfigDesc_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,1,1,4),_CtFDDIMuxConfigDesc_Type())
ctFDDIMuxConfigDesc.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIMuxConfigDesc.setStatus(_A)
_CtFDDIMuxCapEnableTable_Object=MibTable
ctFDDIMuxCapEnableTable=_CtFDDIMuxCapEnableTable_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,2))
if mibBuilder.loadTexts:ctFDDIMuxCapEnableTable.setStatus(_A)
_CtFDDIMuxCapEnableEntry_Object=MibTableRow
ctFDDIMuxCapEnableEntry=_CtFDDIMuxCapEnableEntry_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,2,1))
ctFDDIMuxCapEnableEntry.setIndexNames((0,_C,_P))
if mibBuilder.loadTexts:ctFDDIMuxCapEnableEntry.setStatus(_A)
class _CtFDDIMuxEnableSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,256))
_CtFDDIMuxEnableSlot_Type.__name__=_D
_CtFDDIMuxEnableSlot_Object=MibTableColumn
ctFDDIMuxEnableSlot=_CtFDDIMuxEnableSlot_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,2,1,1),_CtFDDIMuxEnableSlot_Type())
ctFDDIMuxEnableSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIMuxEnableSlot.setStatus(_A)
_CtFDDIMuxCapEnable_Type=Integer32
_CtFDDIMuxCapEnable_Object=MibTableColumn
ctFDDIMuxCapEnable=_CtFDDIMuxCapEnable_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,2,1,2),_CtFDDIMuxCapEnable_Type())
ctFDDIMuxCapEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:ctFDDIMuxCapEnable.setStatus(_A)
_CtFDDIMuxMasterPortAssignmentChange_Type=Counter32
_CtFDDIMuxMasterPortAssignmentChange_Object=MibTableColumn
ctFDDIMuxMasterPortAssignmentChange=_CtFDDIMuxMasterPortAssignmentChange_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,2,1,3),_CtFDDIMuxMasterPortAssignmentChange_Type())
ctFDDIMuxMasterPortAssignmentChange.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIMuxMasterPortAssignmentChange.setStatus(_A)
_CtFDDIMuxOutTable_Object=MibTable
ctFDDIMuxOutTable=_CtFDDIMuxOutTable_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,3))
if mibBuilder.loadTexts:ctFDDIMuxOutTable.setStatus(_A)
_CtFDDIMuxOutEntry_Object=MibTableRow
ctFDDIMuxOutEntry=_CtFDDIMuxOutEntry_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,3,1))
ctFDDIMuxOutEntry.setIndexNames((0,_C,_Q),(0,_C,_R))
if mibBuilder.loadTexts:ctFDDIMuxOutEntry.setStatus(_A)
class _CtFDDIMuxOutSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CtFDDIMuxOutSlot_Type.__name__=_D
_CtFDDIMuxOutSlot_Object=MibTableColumn
ctFDDIMuxOutSlot=_CtFDDIMuxOutSlot_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,3,1,1),_CtFDDIMuxOutSlot_Type())
ctFDDIMuxOutSlot.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIMuxOutSlot.setStatus(_A)
_CtFDDIMuxOutID_Type=Integer32
_CtFDDIMuxOutID_Object=MibTableColumn
ctFDDIMuxOutID=_CtFDDIMuxOutID_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,3,1,2),_CtFDDIMuxOutID_Type())
ctFDDIMuxOutID.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIMuxOutID.setStatus(_A)
class _CtFDDIMuxOutMACIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtFDDIMuxOutMACIndex_Type.__name__=_D
_CtFDDIMuxOutMACIndex_Object=MibTableColumn
ctFDDIMuxOutMACIndex=_CtFDDIMuxOutMACIndex_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,3,1,3),_CtFDDIMuxOutMACIndex_Type())
ctFDDIMuxOutMACIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIMuxOutMACIndex.setStatus(_A)
class _CtFDDIMuxOutSMTIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtFDDIMuxOutSMTIndex_Type.__name__=_D
_CtFDDIMuxOutSMTIndex_Object=MibTableColumn
ctFDDIMuxOutSMTIndex=_CtFDDIMuxOutSMTIndex_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,3,1,4),_CtFDDIMuxOutSMTIndex_Type())
ctFDDIMuxOutSMTIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIMuxOutSMTIndex.setStatus(_A)
_CtFDDIMuxBytes_Type=Integer32
_CtFDDIMuxBytes_Object=MibTableColumn
ctFDDIMuxBytes=_CtFDDIMuxBytes_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,3,1,5),_CtFDDIMuxBytes_Type())
ctFDDIMuxBytes.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIMuxBytes.setStatus(_A)
_CtFDDIMuxFrames_Type=Integer32
_CtFDDIMuxFrames_Object=MibTableColumn
ctFDDIMuxFrames=_CtFDDIMuxFrames_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,3,1,6),_CtFDDIMuxFrames_Type())
ctFDDIMuxFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIMuxFrames.setStatus(_A)
_CtFDDIMuxMasterPortTable_Object=MibTable
ctFDDIMuxMasterPortTable=_CtFDDIMuxMasterPortTable_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,4))
if mibBuilder.loadTexts:ctFDDIMuxMasterPortTable.setStatus(_A)
_CtFDDIMuxMasterPortEntry_Object=MibTableRow
ctFDDIMuxMasterPortEntry=_CtFDDIMuxMasterPortEntry_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,4,1))
ctFDDIMuxMasterPortEntry.setIndexNames((0,_C,_S),(0,_C,_T))
if mibBuilder.loadTexts:ctFDDIMuxMasterPortEntry.setStatus(_A)
class _CtFDDIMuxMasterPortSlotID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_CtFDDIMuxMasterPortSlotID_Type.__name__=_D
_CtFDDIMuxMasterPortSlotID_Object=MibTableColumn
ctFDDIMuxMasterPortSlotID=_CtFDDIMuxMasterPortSlotID_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,4,1,1),_CtFDDIMuxMasterPortSlotID_Type())
ctFDDIMuxMasterPortSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIMuxMasterPortSlotID.setStatus(_A)
class _CtFDDIMuxMasterPortID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtFDDIMuxMasterPortID_Type.__name__=_D
_CtFDDIMuxMasterPortID_Object=MibTableColumn
ctFDDIMuxMasterPortID=_CtFDDIMuxMasterPortID_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,4,1,2),_CtFDDIMuxMasterPortID_Type())
ctFDDIMuxMasterPortID.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIMuxMasterPortID.setStatus(_A)
_CtFDDIMuxMasterPortAssignment_Type=Integer32
_CtFDDIMuxMasterPortAssignment_Object=MibTableColumn
ctFDDIMuxMasterPortAssignment=_CtFDDIMuxMasterPortAssignment_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,4,1,3),_CtFDDIMuxMasterPortAssignment_Type())
ctFDDIMuxMasterPortAssignment.setMaxAccess(_E)
if mibBuilder.loadTexts:ctFDDIMuxMasterPortAssignment.setStatus(_A)
class _CtFDDIMuxMasterPortIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_CtFDDIMuxMasterPortIndex_Type.__name__=_D
_CtFDDIMuxMasterPortIndex_Object=MibTableColumn
ctFDDIMuxMasterPortIndex=_CtFDDIMuxMasterPortIndex_Object((1,3,6,1,4,1,52,4,1,2,5,1,3,4,1,4),_CtFDDIMuxMasterPortIndex_Type())
ctFDDIMuxMasterPortIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDIMuxMasterPortIndex.setStatus(_A)
_CtFDDISerialConfig_ObjectIdentity=ObjectIdentity
ctFDDISerialConfig=_CtFDDISerialConfig_ObjectIdentity((1,3,6,1,4,1,52,4,1,2,5,1,4))
class _CtFDDINumbModules_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14))
_CtFDDINumbModules_Type.__name__=_D
_CtFDDINumbModules_Object=MibScalar
ctFDDINumbModules=_CtFDDINumbModules_Object((1,3,6,1,4,1,52,4,1,2,5,1,4,1),_CtFDDINumbModules_Type())
ctFDDINumbModules.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDINumbModules.setStatus(_A)
_CtFDDISerialConfigTable_Object=MibTable
ctFDDISerialConfigTable=_CtFDDISerialConfigTable_Object((1,3,6,1,4,1,52,4,1,2,5,1,4,2))
if mibBuilder.loadTexts:ctFDDISerialConfigTable.setStatus(_A)
_CtFDDISerialConfigEntry_Object=MibTableRow
ctFDDISerialConfigEntry=_CtFDDISerialConfigEntry_Object((1,3,6,1,4,1,52,4,1,2,5,1,4,2,1))
ctFDDISerialConfigEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:ctFDDISerialConfigEntry.setStatus(_A)
_CtFDDISerialSlotID_Type=Integer32
_CtFDDISerialSlotID_Object=MibTableColumn
ctFDDISerialSlotID=_CtFDDISerialSlotID_Object((1,3,6,1,4,1,52,4,1,2,5,1,4,2,1,1),_CtFDDISerialSlotID_Type())
ctFDDISerialSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDISerialSlotID.setStatus(_A)
class _CtFDDISerialAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_Y,4),('hwControlFNB1',5),('hwControlFNB2',6),('hwControl',7)))
_CtFDDISerialAdminStatus_Type.__name__=_D
_CtFDDISerialAdminStatus_Object=MibTableColumn
ctFDDISerialAdminStatus=_CtFDDISerialAdminStatus_Object((1,3,6,1,4,1,52,4,1,2,5,1,4,2,1,2),_CtFDDISerialAdminStatus_Type())
ctFDDISerialAdminStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:ctFDDISerialAdminStatus.setStatus(_A)
class _CtFDDISerialOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_V,1),(_W,2),(_X,3),(_Y,4)))
_CtFDDISerialOperStatus_Type.__name__=_D
_CtFDDISerialOperStatus_Object=MibTableColumn
ctFDDISerialOperStatus=_CtFDDISerialOperStatus_Object((1,3,6,1,4,1,52,4,1,2,5,1,4,2,1,3),_CtFDDISerialOperStatus_Type())
ctFDDISerialOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFDDISerialOperStatus.setStatus(_A)
_CtFDDIModuleFPIMTable_Object=MibTable
ctFDDIModuleFPIMTable=_CtFDDIModuleFPIMTable_Object((1,3,6,1,4,1,52,4,1,2,5,1,4,3))
if mibBuilder.loadTexts:ctFDDIModuleFPIMTable.setStatus(_A)
_CtFDDIModuleFPIMEntry_Object=MibTableRow
ctFDDIModuleFPIMEntry=_CtFDDIModuleFPIMEntry_Object((1,3,6,1,4,1,52,4,1,2,5,1,4,3,1))
ctFDDIModuleFPIMEntry.setIndexNames((0,_C,_Z),(0,_C,_a))
if mibBuilder.loadTexts:ctFDDIModuleFPIMEntry.setStatus(_A)
_CtFddiFPIMSlotID_Type=Integer32
_CtFddiFPIMSlotID_Object=MibTableColumn
ctFddiFPIMSlotID=_CtFddiFPIMSlotID_Object((1,3,6,1,4,1,52,4,1,2,5,1,4,3,1,1),_CtFddiFPIMSlotID_Type())
ctFddiFPIMSlotID.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFddiFPIMSlotID.setStatus(_A)
_CtFddiFPIM_Type=Integer32
_CtFddiFPIM_Object=MibTableColumn
ctFddiFPIM=_CtFddiFPIM_Object((1,3,6,1,4,1,52,4,1,2,5,1,4,3,1,2),_CtFddiFPIM_Type())
ctFddiFPIM.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFddiFPIM.setStatus(_A)
class _CtFddiFPIMStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('link',1),('noLink',2),('notSupported',3)))
_CtFddiFPIMStatus_Type.__name__=_D
_CtFddiFPIMStatus_Object=MibTableColumn
ctFddiFPIMStatus=_CtFddiFPIMStatus_Object((1,3,6,1,4,1,52,4,1,2,5,1,4,3,1,4),_CtFddiFPIMStatus_Type())
ctFddiFPIMStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFddiFPIMStatus.setStatus(_A)
_CtFddiFPIMType_Type=ObjectIdentifier
_CtFddiFPIMType_Object=MibTableColumn
ctFddiFPIMType=_CtFddiFPIMType_Object((1,3,6,1,4,1,52,4,1,2,5,1,4,3,1,5),_CtFddiFPIMType_Type())
ctFddiFPIMType.setMaxAccess(_B)
if mibBuilder.loadTexts:ctFddiFPIMType.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'ctFDDIResource':ctFDDIResource,'ctFDDIResourceTable':ctFDDIResourceTable,'ctFDDIResourceEntry':ctFDDIResourceEntry,_F:ctFDDIResourceSlotID,_G:ctFDDIResourceID,'ctFDDIResourceType':ctFDDIResourceType,'ctFDDIResourceNumbInstance':ctFDDIResourceNumbInstance,'ctFDDINonMux':ctFDDINonMux,'ctFDDINonMuxCapTable':ctFDDINonMuxCapTable,'ctFDDINonMuxCapEntry':ctFDDINonMuxCapEntry,_H:ctFDDINMSlot,_I:ctFDDINMConfigID,'ctFDDINMConfig':ctFDDINMConfig,'ctFDDINMConfigDesc':ctFDDINMConfigDesc,'ctFDDINonMuxCapEnableTable':ctFDDINonMuxCapEnableTable,'ctFDDINonMuxCapEnableEntry':ctFDDINonMuxCapEnableEntry,_J:ctFDDINMEnableSlot,'ctFDDINMCapEnable':ctFDDINMCapEnable,'ctFDDINonMuxConnectionTable':ctFDDINonMuxConnectionTable,'ctFDDINonMuxConnectionEntry':ctFDDINonMuxConnectionEntry,_K:ctFDDINMConnectionSlot,_L:ctFDDINMConnectionID,'ctFDDINMSMT':ctFDDINMSMT,'ctFDDINMMAC':ctFDDINMMAC,'ctFDDINMBytes':ctFDDINMBytes,'ctFDDINMFrames':ctFDDINMFrames,'ctFDDINonMuxInterfaceTable':ctFDDINonMuxInterfaceTable,'ctFDDINonMuxInterfaceEntry':ctFDDINonMuxInterfaceEntry,_M:ctFDDINMInterSlot,'ctFDDINMNumbInterfaces':ctFDDINMNumbInterfaces,'ctFDDIMux':ctFDDIMux,'ctFDDIMuxCapTable':ctFDDIMuxCapTable,'ctFDDIMuxCapEntry':ctFDDIMuxCapEntry,_N:ctFDDIMuxSlot,'ctFDDIMuxConfigID':ctFDDIMuxConfigID,_O:ctFDDIMuxConfig,'ctFDDIMuxConfigDesc':ctFDDIMuxConfigDesc,'ctFDDIMuxCapEnableTable':ctFDDIMuxCapEnableTable,'ctFDDIMuxCapEnableEntry':ctFDDIMuxCapEnableEntry,_P:ctFDDIMuxEnableSlot,'ctFDDIMuxCapEnable':ctFDDIMuxCapEnable,'ctFDDIMuxMasterPortAssignmentChange':ctFDDIMuxMasterPortAssignmentChange,'ctFDDIMuxOutTable':ctFDDIMuxOutTable,'ctFDDIMuxOutEntry':ctFDDIMuxOutEntry,_Q:ctFDDIMuxOutSlot,_R:ctFDDIMuxOutID,'ctFDDIMuxOutMACIndex':ctFDDIMuxOutMACIndex,'ctFDDIMuxOutSMTIndex':ctFDDIMuxOutSMTIndex,'ctFDDIMuxBytes':ctFDDIMuxBytes,'ctFDDIMuxFrames':ctFDDIMuxFrames,'ctFDDIMuxMasterPortTable':ctFDDIMuxMasterPortTable,'ctFDDIMuxMasterPortEntry':ctFDDIMuxMasterPortEntry,_S:ctFDDIMuxMasterPortSlotID,_T:ctFDDIMuxMasterPortID,'ctFDDIMuxMasterPortAssignment':ctFDDIMuxMasterPortAssignment,'ctFDDIMuxMasterPortIndex':ctFDDIMuxMasterPortIndex,'ctFDDISerialConfig':ctFDDISerialConfig,'ctFDDINumbModules':ctFDDINumbModules,'ctFDDISerialConfigTable':ctFDDISerialConfigTable,'ctFDDISerialConfigEntry':ctFDDISerialConfigEntry,_U:ctFDDISerialSlotID,'ctFDDISerialAdminStatus':ctFDDISerialAdminStatus,'ctFDDISerialOperStatus':ctFDDISerialOperStatus,'ctFDDIModuleFPIMTable':ctFDDIModuleFPIMTable,'ctFDDIModuleFPIMEntry':ctFDDIModuleFPIMEntry,_Z:ctFddiFPIMSlotID,_a:ctFddiFPIM,'ctFddiFPIMStatus':ctFddiFPIMStatus,'ctFddiFPIMType':ctFddiFPIMType})