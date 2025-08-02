_Z='pxmEthIntfGroup'
_Y='pxmEthIntfCSFAsTDATrigger'
_X='pxmEthIntfMacAddress'
_W='pxmEthIntfLoopbackBehavior'
_V='pxmEthIntfAvailableBW'
_U='pxmEthIntfMaxReservableBW'
_T='pxmEthIntfOverBookingFactor'
_S='pxmEthIntfAcceptableFrameType'
_R='pxmEthIntfInterfaceRate'
_Q='pxmEthIntfTerminalTestSignalMon'
_P='pxmEthIntfTerminalTestSignalGen'
_O='pxmEthIntfFacTestSignalMon'
_N='pxmEthIntfFacTestSignalGen'
_M='pxmEthIntfIngressTrafficClass'
_L='pxmEthIntfDefaultPriority'
_K='pxmEthIntfDefaultVLANID'
_J='pxmEthIntfInnerTPID'
_I='pxmEthIntfOuterTPID'
_H='pxmEthIntfInterfaceType'
_G='pxmEthIntfMTUSize'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='read-write'
_B='INFINERA-TP-PXMETHINTF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatHundredths,FloatTenths,InfnAcceptableFrameType,InfnEnableDisableType,InfnLoopbackBehavior,InfnPXMInterfaceType=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','FloatTenths','InfnAcceptableFrameType','InfnEnableDisableType','InfnLoopbackBehavior','InfnPXMInterfaceType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pxmEthIntfMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,76))
if mibBuilder.loadTexts:pxmEthIntfMIB.setRevisions(('2016-05-20 00:00',))
_PxmEthIntfTable_Object=MibTable
pxmEthIntfTable=_PxmEthIntfTable_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1))
if mibBuilder.loadTexts:pxmEthIntfTable.setStatus(_A)
_PxmEthIntfEntry_Object=MibTableRow
pxmEthIntfEntry=_PxmEthIntfEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1))
pxmEthIntfEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:pxmEthIntfEntry.setStatus(_A)
_PxmEthIntfMTUSize_Type=Integer32
_PxmEthIntfMTUSize_Object=MibTableColumn
pxmEthIntfMTUSize=_PxmEthIntfMTUSize_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,1),_PxmEthIntfMTUSize_Type())
pxmEthIntfMTUSize.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmEthIntfMTUSize.setStatus(_A)
_PxmEthIntfInterfaceType_Type=InfnPXMInterfaceType
_PxmEthIntfInterfaceType_Object=MibTableColumn
pxmEthIntfInterfaceType=_PxmEthIntfInterfaceType_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,2),_PxmEthIntfInterfaceType_Type())
pxmEthIntfInterfaceType.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmEthIntfInterfaceType.setStatus(_A)
_PxmEthIntfOuterTPID_Type=Integer32
_PxmEthIntfOuterTPID_Object=MibTableColumn
pxmEthIntfOuterTPID=_PxmEthIntfOuterTPID_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,3),_PxmEthIntfOuterTPID_Type())
pxmEthIntfOuterTPID.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmEthIntfOuterTPID.setStatus(_A)
_PxmEthIntfInnerTPID_Type=Integer32
_PxmEthIntfInnerTPID_Object=MibTableColumn
pxmEthIntfInnerTPID=_PxmEthIntfInnerTPID_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,4),_PxmEthIntfInnerTPID_Type())
pxmEthIntfInnerTPID.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmEthIntfInnerTPID.setStatus(_A)
_PxmEthIntfDefaultVLANID_Type=Integer32
_PxmEthIntfDefaultVLANID_Object=MibTableColumn
pxmEthIntfDefaultVLANID=_PxmEthIntfDefaultVLANID_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,5),_PxmEthIntfDefaultVLANID_Type())
pxmEthIntfDefaultVLANID.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmEthIntfDefaultVLANID.setStatus(_A)
_PxmEthIntfDefaultPriority_Type=Integer32
_PxmEthIntfDefaultPriority_Object=MibTableColumn
pxmEthIntfDefaultPriority=_PxmEthIntfDefaultPriority_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,6),_PxmEthIntfDefaultPriority_Type())
pxmEthIntfDefaultPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmEthIntfDefaultPriority.setStatus(_A)
_PxmEthIntfIngressTrafficClass_Type=Integer32
_PxmEthIntfIngressTrafficClass_Object=MibTableColumn
pxmEthIntfIngressTrafficClass=_PxmEthIntfIngressTrafficClass_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,7),_PxmEthIntfIngressTrafficClass_Type())
pxmEthIntfIngressTrafficClass.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmEthIntfIngressTrafficClass.setStatus(_A)
_PxmEthIntfFacTestSignalGen_Type=InfnEnableDisableType
_PxmEthIntfFacTestSignalGen_Object=MibTableColumn
pxmEthIntfFacTestSignalGen=_PxmEthIntfFacTestSignalGen_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,8),_PxmEthIntfFacTestSignalGen_Type())
pxmEthIntfFacTestSignalGen.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmEthIntfFacTestSignalGen.setStatus(_A)
_PxmEthIntfFacTestSignalMon_Type=InfnEnableDisableType
_PxmEthIntfFacTestSignalMon_Object=MibTableColumn
pxmEthIntfFacTestSignalMon=_PxmEthIntfFacTestSignalMon_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,9),_PxmEthIntfFacTestSignalMon_Type())
pxmEthIntfFacTestSignalMon.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmEthIntfFacTestSignalMon.setStatus(_A)
_PxmEthIntfTerminalTestSignalGen_Type=InfnEnableDisableType
_PxmEthIntfTerminalTestSignalGen_Object=MibTableColumn
pxmEthIntfTerminalTestSignalGen=_PxmEthIntfTerminalTestSignalGen_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,10),_PxmEthIntfTerminalTestSignalGen_Type())
pxmEthIntfTerminalTestSignalGen.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmEthIntfTerminalTestSignalGen.setStatus(_A)
_PxmEthIntfTerminalTestSignalMon_Type=InfnEnableDisableType
_PxmEthIntfTerminalTestSignalMon_Object=MibTableColumn
pxmEthIntfTerminalTestSignalMon=_PxmEthIntfTerminalTestSignalMon_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,11),_PxmEthIntfTerminalTestSignalMon_Type())
pxmEthIntfTerminalTestSignalMon.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmEthIntfTerminalTestSignalMon.setStatus(_A)
_PxmEthIntfInterfaceRate_Type=Integer32
_PxmEthIntfInterfaceRate_Object=MibTableColumn
pxmEthIntfInterfaceRate=_PxmEthIntfInterfaceRate_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,12),_PxmEthIntfInterfaceRate_Type())
pxmEthIntfInterfaceRate.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmEthIntfInterfaceRate.setStatus(_A)
_PxmEthIntfAcceptableFrameType_Type=InfnAcceptableFrameType
_PxmEthIntfAcceptableFrameType_Object=MibTableColumn
pxmEthIntfAcceptableFrameType=_PxmEthIntfAcceptableFrameType_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,13),_PxmEthIntfAcceptableFrameType_Type())
pxmEthIntfAcceptableFrameType.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmEthIntfAcceptableFrameType.setStatus(_A)
_PxmEthIntfOverBookingFactor_Type=FloatTenths
_PxmEthIntfOverBookingFactor_Object=MibTableColumn
pxmEthIntfOverBookingFactor=_PxmEthIntfOverBookingFactor_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,14),_PxmEthIntfOverBookingFactor_Type())
pxmEthIntfOverBookingFactor.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmEthIntfOverBookingFactor.setStatus(_A)
_PxmEthIntfMaxReservableBW_Type=FloatHundredths
_PxmEthIntfMaxReservableBW_Object=MibTableColumn
pxmEthIntfMaxReservableBW=_PxmEthIntfMaxReservableBW_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,15),_PxmEthIntfMaxReservableBW_Type())
pxmEthIntfMaxReservableBW.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmEthIntfMaxReservableBW.setStatus(_A)
_PxmEthIntfAvailableBW_Type=FloatHundredths
_PxmEthIntfAvailableBW_Object=MibTableColumn
pxmEthIntfAvailableBW=_PxmEthIntfAvailableBW_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,16),_PxmEthIntfAvailableBW_Type())
pxmEthIntfAvailableBW.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmEthIntfAvailableBW.setStatus(_A)
_PxmEthIntfLoopbackBehavior_Type=InfnLoopbackBehavior
_PxmEthIntfLoopbackBehavior_Object=MibTableColumn
pxmEthIntfLoopbackBehavior=_PxmEthIntfLoopbackBehavior_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,17),_PxmEthIntfLoopbackBehavior_Type())
pxmEthIntfLoopbackBehavior.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmEthIntfLoopbackBehavior.setStatus(_A)
_PxmEthIntfMacAddress_Type=DisplayString
_PxmEthIntfMacAddress_Object=MibTableColumn
pxmEthIntfMacAddress=_PxmEthIntfMacAddress_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,18),_PxmEthIntfMacAddress_Type())
pxmEthIntfMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmEthIntfMacAddress.setStatus(_A)
_PxmEthIntfCSFAsTDATrigger_Type=InfnEnableDisableType
_PxmEthIntfCSFAsTDATrigger_Object=MibTableColumn
pxmEthIntfCSFAsTDATrigger=_PxmEthIntfCSFAsTDATrigger_Object((1,3,6,1,4,1,21296,2,2,2,2,76,1,1,19),_PxmEthIntfCSFAsTDATrigger_Type())
pxmEthIntfCSFAsTDATrigger.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmEthIntfCSFAsTDATrigger.setStatus(_A)
_PxmEthIntfConformance_ObjectIdentity=ObjectIdentity
pxmEthIntfConformance=_PxmEthIntfConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,76,3))
_PxmEthIntfCompliances_ObjectIdentity=ObjectIdentity
pxmEthIntfCompliances=_PxmEthIntfCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,76,3,1))
_PxmEthIntfGroups_ObjectIdentity=ObjectIdentity
pxmEthIntfGroups=_PxmEthIntfGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,76,3,2))
pxmEthIntfGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,76,3,2,1))
pxmEthIntfGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y)))
if mibBuilder.loadTexts:pxmEthIntfGroup.setStatus(_A)
pxmEthIntfCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,76,3,1,1))
pxmEthIntfCompliance.setObjects((_B,_Z))
if mibBuilder.loadTexts:pxmEthIntfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pxmEthIntfMIB':pxmEthIntfMIB,'pxmEthIntfTable':pxmEthIntfTable,'pxmEthIntfEntry':pxmEthIntfEntry,_G:pxmEthIntfMTUSize,_H:pxmEthIntfInterfaceType,_I:pxmEthIntfOuterTPID,_J:pxmEthIntfInnerTPID,_K:pxmEthIntfDefaultVLANID,_L:pxmEthIntfDefaultPriority,_M:pxmEthIntfIngressTrafficClass,_N:pxmEthIntfFacTestSignalGen,_O:pxmEthIntfFacTestSignalMon,_P:pxmEthIntfTerminalTestSignalGen,_Q:pxmEthIntfTerminalTestSignalMon,_R:pxmEthIntfInterfaceRate,_S:pxmEthIntfAcceptableFrameType,_T:pxmEthIntfOverBookingFactor,_U:pxmEthIntfMaxReservableBW,_V:pxmEthIntfAvailableBW,_W:pxmEthIntfLoopbackBehavior,_X:pxmEthIntfMacAddress,_Y:pxmEthIntfCSFAsTDATrigger,'pxmEthIntfConformance':pxmEthIntfConformance,'pxmEthIntfCompliances':pxmEthIntfCompliances,'pxmEthIntfCompliance':pxmEthIntfCompliance,'pxmEthIntfGroups':pxmEthIntfGroups,_Z:pxmEthIntfGroup})