_b='mpWredATMStatPrecValue'
_a='mpWredFRStatPrecValue'
_Z='mpWredIFStatPrecValue'
_Y='mpWredATMPrecCfgValue'
_X='mpWredFRPrecCfgValue'
_W='mpWredIFPrecCfgValue'
_V='mpWredGroupPrecCfgValue'
_U='mpWredGroupCfgName'
_T='mpWredATMCfgVCI'
_S='mpWredATMCfgVPI'
_R='mpWredFRCfgDLCI'
_Q='redUserDefault'
_P='redDefault'
_O='mplsExp'
_N='atmClp'
_M='l2Cos'
_L='discardClass'
_K='dscp'
_J='precedence'
_I='Unsigned32'
_H='DisplayString'
_G='ifIndex'
_F='not-accessible'
_E='packets'
_D='Integer32'
_C='MAIPU-WRED-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mpMgmt,=mibBuilder.importSymbols('MAIPU-SMI','mpMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'enterprises','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime',_H,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
maipuWredMIB=ModuleIdentity((1,3,6,1,4,1,5651,6,2,3,2))
_Maipu_ObjectIdentity=ObjectIdentity
maipu=_Maipu_ObjectIdentity((1,3,6,1,4,1,5651))
_MpMgmt2_ObjectIdentity=ObjectIdentity
mpMgmt2=_MpMgmt2_ObjectIdentity((1,3,6,1,4,1,5651,6))
_MpRouterTech_ObjectIdentity=ObjectIdentity
mpRouterTech=_MpRouterTech_ObjectIdentity((1,3,6,1,4,1,5651,6,2))
_MpRtQoSv2_ObjectIdentity=ObjectIdentity
mpRtQoSv2=_MpRtQoSv2_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3))
_MaipuWredMIBObjects_ObjectIdentity=ObjectIdentity
maipuWredMIBObjects=_MaipuWredMIBObjects_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,2,1))
_MpWredConfig_ObjectIdentity=ObjectIdentity
mpWredConfig=_MpWredConfig_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,2,1,1))
_MpWredGroupCfgTable_Object=MibTable
mpWredGroupCfgTable=_MpWredGroupCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,1))
if mibBuilder.loadTexts:mpWredGroupCfgTable.setStatus(_A)
_MpWredGroupCfgEntry_Object=MibTableRow
mpWredGroupCfgEntry=_MpWredGroupCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,1,1))
mpWredGroupCfgEntry.setIndexNames((0,_C,_U))
if mibBuilder.loadTexts:mpWredGroupCfgEntry.setStatus(_A)
class _MpWredGroupCfgName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpWredGroupCfgName_Type.__name__=_H
_MpWredGroupCfgName_Object=MibTableColumn
mpWredGroupCfgName=_MpWredGroupCfgName_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,1,1,1),_MpWredGroupCfgName_Type())
mpWredGroupCfgName.setMaxAccess(_F)
if mibBuilder.loadTexts:mpWredGroupCfgName.setStatus(_A)
class _MpWredGroupCfgDscpPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8)))
_MpWredGroupCfgDscpPrec_Type.__name__=_D
_MpWredGroupCfgDscpPrec_Object=MibTableColumn
mpWredGroupCfgDscpPrec=_MpWredGroupCfgDscpPrec_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,1,1,2),_MpWredGroupCfgDscpPrec_Type())
mpWredGroupCfgDscpPrec.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredGroupCfgDscpPrec.setStatus(_A)
class _MpWredGroupCfgExponWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_MpWredGroupCfgExponWeight_Type.__name__=_D
_MpWredGroupCfgExponWeight_Object=MibTableColumn
mpWredGroupCfgExponWeight=_MpWredGroupCfgExponWeight_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,1,1,3),_MpWredGroupCfgExponWeight_Type())
mpWredGroupCfgExponWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredGroupCfgExponWeight.setStatus(_A)
_MpWredGroupPrecCfgTable_Object=MibTable
mpWredGroupPrecCfgTable=_MpWredGroupPrecCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,2))
if mibBuilder.loadTexts:mpWredGroupPrecCfgTable.setStatus(_A)
_MpWredGroupPrecCfgEntry_Object=MibTableRow
mpWredGroupPrecCfgEntry=_MpWredGroupPrecCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,2,1))
mpWredGroupPrecCfgEntry.setIndexNames((0,_C,_U),(0,_C,_V))
if mibBuilder.loadTexts:mpWredGroupPrecCfgEntry.setStatus(_A)
class _MpWredGroupPrecCfgValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_MpWredGroupPrecCfgValue_Type.__name__=_D
_MpWredGroupPrecCfgValue_Object=MibTableColumn
mpWredGroupPrecCfgValue=_MpWredGroupPrecCfgValue_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,2,1,1),_MpWredGroupPrecCfgValue_Type())
mpWredGroupPrecCfgValue.setMaxAccess(_F)
if mibBuilder.loadTexts:mpWredGroupPrecCfgValue.setStatus(_A)
_MpWredGroupPrecCfgMinThreshold_Type=Unsigned32
_MpWredGroupPrecCfgMinThreshold_Object=MibTableColumn
mpWredGroupPrecCfgMinThreshold=_MpWredGroupPrecCfgMinThreshold_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,2,1,2),_MpWredGroupPrecCfgMinThreshold_Type())
mpWredGroupPrecCfgMinThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredGroupPrecCfgMinThreshold.setStatus(_A)
if mibBuilder.loadTexts:mpWredGroupPrecCfgMinThreshold.setUnits(_E)
_MpWredGroupPrecCfgMaxThreshold_Type=Unsigned32
_MpWredGroupPrecCfgMaxThreshold_Object=MibTableColumn
mpWredGroupPrecCfgMaxThreshold=_MpWredGroupPrecCfgMaxThreshold_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,2,1,3),_MpWredGroupPrecCfgMaxThreshold_Type())
mpWredGroupPrecCfgMaxThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredGroupPrecCfgMaxThreshold.setStatus(_A)
if mibBuilder.loadTexts:mpWredGroupPrecCfgMaxThreshold.setUnits(_E)
class _MpWredGroupPrecCfgPktDropProb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_MpWredGroupPrecCfgPktDropProb_Type.__name__=_D
_MpWredGroupPrecCfgPktDropProb_Object=MibTableColumn
mpWredGroupPrecCfgPktDropProb=_MpWredGroupPrecCfgPktDropProb_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,2,1,4),_MpWredGroupPrecCfgPktDropProb_Type())
mpWredGroupPrecCfgPktDropProb.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredGroupPrecCfgPktDropProb.setStatus(_A)
_MpWredInterfaceCfgTable_Object=MibTable
mpWredInterfaceCfgTable=_MpWredInterfaceCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,3))
if mibBuilder.loadTexts:mpWredInterfaceCfgTable.setStatus(_A)
_MpWredInterfaceCfgEntry_Object=MibTableRow
mpWredInterfaceCfgEntry=_MpWredInterfaceCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,3,1))
mpWredInterfaceCfgEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:mpWredInterfaceCfgEntry.setStatus(_A)
class _MpWredIFCfgGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpWredIFCfgGroupName_Type.__name__=_H
_MpWredIFCfgGroupName_Object=MibTableColumn
mpWredIFCfgGroupName=_MpWredIFCfgGroupName_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,3,1,1),_MpWredIFCfgGroupName_Type())
mpWredIFCfgGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredIFCfgGroupName.setStatus(_A)
class _MpWredIFCfgDscpPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8)))
_MpWredIFCfgDscpPrec_Type.__name__=_D
_MpWredIFCfgDscpPrec_Object=MibTableColumn
mpWredIFCfgDscpPrec=_MpWredIFCfgDscpPrec_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,3,1,2),_MpWredIFCfgDscpPrec_Type())
mpWredIFCfgDscpPrec.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredIFCfgDscpPrec.setStatus(_A)
class _MpWredIFCfgExponWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_MpWredIFCfgExponWeight_Type.__name__=_D
_MpWredIFCfgExponWeight_Object=MibTableColumn
mpWredIFCfgExponWeight=_MpWredIFCfgExponWeight_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,3,1,3),_MpWredIFCfgExponWeight_Type())
mpWredIFCfgExponWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredIFCfgExponWeight.setStatus(_A)
_MpWredFrameRelayVCCfgTable_Object=MibTable
mpWredFrameRelayVCCfgTable=_MpWredFrameRelayVCCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,4))
if mibBuilder.loadTexts:mpWredFrameRelayVCCfgTable.setStatus(_A)
_MpWredFrameRelayVCCfgEntry_Object=MibTableRow
mpWredFrameRelayVCCfgEntry=_MpWredFrameRelayVCCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,4,1))
mpWredFrameRelayVCCfgEntry.setIndexNames((0,_C,_G),(0,_C,_R))
if mibBuilder.loadTexts:mpWredFrameRelayVCCfgEntry.setStatus(_A)
class _MpWredFRCfgDLCI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1007))
_MpWredFRCfgDLCI_Type.__name__=_I
_MpWredFRCfgDLCI_Object=MibTableColumn
mpWredFRCfgDLCI=_MpWredFRCfgDLCI_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,4,1,1),_MpWredFRCfgDLCI_Type())
mpWredFRCfgDLCI.setMaxAccess(_F)
if mibBuilder.loadTexts:mpWredFRCfgDLCI.setStatus(_A)
class _MpWredFRCfgGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpWredFRCfgGroupName_Type.__name__=_H
_MpWredFRCfgGroupName_Object=MibTableColumn
mpWredFRCfgGroupName=_MpWredFRCfgGroupName_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,4,1,2),_MpWredFRCfgGroupName_Type())
mpWredFRCfgGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredFRCfgGroupName.setStatus(_A)
class _MpWredFRCfgDscpPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8)))
_MpWredFRCfgDscpPrec_Type.__name__=_D
_MpWredFRCfgDscpPrec_Object=MibTableColumn
mpWredFRCfgDscpPrec=_MpWredFRCfgDscpPrec_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,4,1,3),_MpWredFRCfgDscpPrec_Type())
mpWredFRCfgDscpPrec.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredFRCfgDscpPrec.setStatus(_A)
class _MpWredFRCfgExponWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_MpWredFRCfgExponWeight_Type.__name__=_D
_MpWredFRCfgExponWeight_Object=MibTableColumn
mpWredFRCfgExponWeight=_MpWredFRCfgExponWeight_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,4,1,4),_MpWredFRCfgExponWeight_Type())
mpWredFRCfgExponWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredFRCfgExponWeight.setStatus(_A)
_MpWredATMPVCCfgTable_Object=MibTable
mpWredATMPVCCfgTable=_MpWredATMPVCCfgTable_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,5))
if mibBuilder.loadTexts:mpWredATMPVCCfgTable.setStatus(_A)
_MpWredATMPVCCfgEntry_Object=MibTableRow
mpWredATMPVCCfgEntry=_MpWredATMPVCCfgEntry_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,5,1))
mpWredATMPVCCfgEntry.setIndexNames((0,_C,_G),(0,_C,_S),(0,_C,_T))
if mibBuilder.loadTexts:mpWredATMPVCCfgEntry.setStatus(_A)
class _MpWredATMCfgVPI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4095))
_MpWredATMCfgVPI_Type.__name__=_I
_MpWredATMCfgVPI_Object=MibTableColumn
mpWredATMCfgVPI=_MpWredATMCfgVPI_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,5,1,1),_MpWredATMCfgVPI_Type())
mpWredATMCfgVPI.setMaxAccess(_F)
if mibBuilder.loadTexts:mpWredATMCfgVPI.setStatus(_A)
class _MpWredATMCfgVCI_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_MpWredATMCfgVCI_Type.__name__=_I
_MpWredATMCfgVCI_Object=MibTableColumn
mpWredATMCfgVCI=_MpWredATMCfgVCI_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,5,1,2),_MpWredATMCfgVCI_Type())
mpWredATMCfgVCI.setMaxAccess(_F)
if mibBuilder.loadTexts:mpWredATMCfgVCI.setStatus(_A)
class _MpWredATMCfgGroupName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_MpWredATMCfgGroupName_Type.__name__=_H
_MpWredATMCfgGroupName_Object=MibTableColumn
mpWredATMCfgGroupName=_MpWredATMCfgGroupName_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,5,1,3),_MpWredATMCfgGroupName_Type())
mpWredATMCfgGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredATMCfgGroupName.setStatus(_A)
class _MpWredATMCfgDscpPrec_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8)))
_MpWredATMCfgDscpPrec_Type.__name__=_D
_MpWredATMCfgDscpPrec_Object=MibTableColumn
mpWredATMCfgDscpPrec=_MpWredATMCfgDscpPrec_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,5,1,4),_MpWredATMCfgDscpPrec_Type())
mpWredATMCfgDscpPrec.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredATMCfgDscpPrec.setStatus(_A)
class _MpWredATMCfgExponWeight_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_MpWredATMCfgExponWeight_Type.__name__=_D
_MpWredATMCfgExponWeight_Object=MibTableColumn
mpWredATMCfgExponWeight=_MpWredATMCfgExponWeight_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,5,1,5),_MpWredATMCfgExponWeight_Type())
mpWredATMCfgExponWeight.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredATMCfgExponWeight.setStatus(_A)
_MpWredCfgInterfacePrecTable_Object=MibTable
mpWredCfgInterfacePrecTable=_MpWredCfgInterfacePrecTable_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,6))
if mibBuilder.loadTexts:mpWredCfgInterfacePrecTable.setStatus(_A)
_MpWredCfgInterfacePrecEntry_Object=MibTableRow
mpWredCfgInterfacePrecEntry=_MpWredCfgInterfacePrecEntry_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,6,1))
mpWredCfgInterfacePrecEntry.setIndexNames((0,_C,_G),(0,_C,_W))
if mibBuilder.loadTexts:mpWredCfgInterfacePrecEntry.setStatus(_A)
class _MpWredIFPrecCfgValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_MpWredIFPrecCfgValue_Type.__name__=_D
_MpWredIFPrecCfgValue_Object=MibTableColumn
mpWredIFPrecCfgValue=_MpWredIFPrecCfgValue_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,6,1,1),_MpWredIFPrecCfgValue_Type())
mpWredIFPrecCfgValue.setMaxAccess(_F)
if mibBuilder.loadTexts:mpWredIFPrecCfgValue.setStatus(_A)
_MpWredIFPrecCfgMinThreshold_Type=Unsigned32
_MpWredIFPrecCfgMinThreshold_Object=MibTableColumn
mpWredIFPrecCfgMinThreshold=_MpWredIFPrecCfgMinThreshold_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,6,1,2),_MpWredIFPrecCfgMinThreshold_Type())
mpWredIFPrecCfgMinThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredIFPrecCfgMinThreshold.setStatus(_A)
if mibBuilder.loadTexts:mpWredIFPrecCfgMinThreshold.setUnits(_E)
_MpWredIFPrecCfgMaxThreshold_Type=Unsigned32
_MpWredIFPrecCfgMaxThreshold_Object=MibTableColumn
mpWredIFPrecCfgMaxThreshold=_MpWredIFPrecCfgMaxThreshold_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,6,1,3),_MpWredIFPrecCfgMaxThreshold_Type())
mpWredIFPrecCfgMaxThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredIFPrecCfgMaxThreshold.setStatus(_A)
if mibBuilder.loadTexts:mpWredIFPrecCfgMaxThreshold.setUnits(_E)
class _MpWredIFPrecCfgPktDropProb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_MpWredIFPrecCfgPktDropProb_Type.__name__=_D
_MpWredIFPrecCfgPktDropProb_Object=MibTableColumn
mpWredIFPrecCfgPktDropProb=_MpWredIFPrecCfgPktDropProb_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,6,1,4),_MpWredIFPrecCfgPktDropProb_Type())
mpWredIFPrecCfgPktDropProb.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredIFPrecCfgPktDropProb.setStatus(_A)
_MpWredCfgFrameRelayVCPrecTable_Object=MibTable
mpWredCfgFrameRelayVCPrecTable=_MpWredCfgFrameRelayVCPrecTable_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,7))
if mibBuilder.loadTexts:mpWredCfgFrameRelayVCPrecTable.setStatus(_A)
_MpWredCfgFrameRelayVCPrecEntry_Object=MibTableRow
mpWredCfgFrameRelayVCPrecEntry=_MpWredCfgFrameRelayVCPrecEntry_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,7,1))
mpWredCfgFrameRelayVCPrecEntry.setIndexNames((0,_C,_G),(0,_C,_R),(0,_C,_X))
if mibBuilder.loadTexts:mpWredCfgFrameRelayVCPrecEntry.setStatus(_A)
class _MpWredFRPrecCfgValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_MpWredFRPrecCfgValue_Type.__name__=_D
_MpWredFRPrecCfgValue_Object=MibTableColumn
mpWredFRPrecCfgValue=_MpWredFRPrecCfgValue_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,7,1,1),_MpWredFRPrecCfgValue_Type())
mpWredFRPrecCfgValue.setMaxAccess(_F)
if mibBuilder.loadTexts:mpWredFRPrecCfgValue.setStatus(_A)
_MpWredFRPrecCfgMinThreshold_Type=Unsigned32
_MpWredFRPrecCfgMinThreshold_Object=MibTableColumn
mpWredFRPrecCfgMinThreshold=_MpWredFRPrecCfgMinThreshold_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,7,1,2),_MpWredFRPrecCfgMinThreshold_Type())
mpWredFRPrecCfgMinThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredFRPrecCfgMinThreshold.setStatus(_A)
if mibBuilder.loadTexts:mpWredFRPrecCfgMinThreshold.setUnits(_E)
_MpWredFRPrecCfgMaxThreshold_Type=Unsigned32
_MpWredFRPrecCfgMaxThreshold_Object=MibTableColumn
mpWredFRPrecCfgMaxThreshold=_MpWredFRPrecCfgMaxThreshold_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,7,1,3),_MpWredFRPrecCfgMaxThreshold_Type())
mpWredFRPrecCfgMaxThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredFRPrecCfgMaxThreshold.setStatus(_A)
if mibBuilder.loadTexts:mpWredFRPrecCfgMaxThreshold.setUnits(_E)
class _MpWredFRPrecCfgPktDropProb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_MpWredFRPrecCfgPktDropProb_Type.__name__=_D
_MpWredFRPrecCfgPktDropProb_Object=MibTableColumn
mpWredFRPrecCfgPktDropProb=_MpWredFRPrecCfgPktDropProb_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,7,1,4),_MpWredFRPrecCfgPktDropProb_Type())
mpWredFRPrecCfgPktDropProb.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredFRPrecCfgPktDropProb.setStatus(_A)
_MpWredCfgATMPVCPrecTable_Object=MibTable
mpWredCfgATMPVCPrecTable=_MpWredCfgATMPVCPrecTable_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,8))
if mibBuilder.loadTexts:mpWredCfgATMPVCPrecTable.setStatus(_A)
_MpWredCfgATMPVCPrecEntry_Object=MibTableRow
mpWredCfgATMPVCPrecEntry=_MpWredCfgATMPVCPrecEntry_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,8,1))
mpWredCfgATMPVCPrecEntry.setIndexNames((0,_C,_G),(0,_C,_S),(0,_C,_T),(0,_C,_Y))
if mibBuilder.loadTexts:mpWredCfgATMPVCPrecEntry.setStatus(_A)
class _MpWredATMPrecCfgValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_MpWredATMPrecCfgValue_Type.__name__=_D
_MpWredATMPrecCfgValue_Object=MibTableColumn
mpWredATMPrecCfgValue=_MpWredATMPrecCfgValue_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,8,1,1),_MpWredATMPrecCfgValue_Type())
mpWredATMPrecCfgValue.setMaxAccess(_F)
if mibBuilder.loadTexts:mpWredATMPrecCfgValue.setStatus(_A)
_MpWredATMPrecCfgMinThreshold_Type=Unsigned32
_MpWredATMPrecCfgMinThreshold_Object=MibTableColumn
mpWredATMPrecCfgMinThreshold=_MpWredATMPrecCfgMinThreshold_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,8,1,2),_MpWredATMPrecCfgMinThreshold_Type())
mpWredATMPrecCfgMinThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredATMPrecCfgMinThreshold.setStatus(_A)
if mibBuilder.loadTexts:mpWredATMPrecCfgMinThreshold.setUnits(_E)
_MpWredATMPrecCfgMaxThreshold_Type=Unsigned32
_MpWredATMPrecCfgMaxThreshold_Object=MibTableColumn
mpWredATMPrecCfgMaxThreshold=_MpWredATMPrecCfgMaxThreshold_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,8,1,3),_MpWredATMPrecCfgMaxThreshold_Type())
mpWredATMPrecCfgMaxThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredATMPrecCfgMaxThreshold.setStatus(_A)
if mibBuilder.loadTexts:mpWredATMPrecCfgMaxThreshold.setUnits(_E)
class _MpWredATMPrecCfgPktDropProb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65536))
_MpWredATMPrecCfgPktDropProb_Type.__name__=_D
_MpWredATMPrecCfgPktDropProb_Object=MibTableColumn
mpWredATMPrecCfgPktDropProb=_MpWredATMPrecCfgPktDropProb_Object((1,3,6,1,4,1,5651,6,2,3,2,1,1,8,1,4),_MpWredATMPrecCfgPktDropProb_Type())
mpWredATMPrecCfgPktDropProb.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredATMPrecCfgPktDropProb.setStatus(_A)
_MpWredStats_ObjectIdentity=ObjectIdentity
mpWredStats=_MpWredStats_ObjectIdentity((1,3,6,1,4,1,5651,6,2,3,2,1,2))
_MpWredInterfaceStatTable_Object=MibTable
mpWredInterfaceStatTable=_MpWredInterfaceStatTable_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,1))
if mibBuilder.loadTexts:mpWredInterfaceStatTable.setStatus(_A)
_MpWredInterfaceStatEntry_Object=MibTableRow
mpWredInterfaceStatEntry=_MpWredInterfaceStatEntry_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,1,1))
mpWredInterfaceStatEntry.setIndexNames((0,_C,_G),(0,_C,_Z))
if mibBuilder.loadTexts:mpWredInterfaceStatEntry.setStatus(_A)
class _MpWredIFStatPrecValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_MpWredIFStatPrecValue_Type.__name__=_D
_MpWredIFStatPrecValue_Object=MibTableColumn
mpWredIFStatPrecValue=_MpWredIFStatPrecValue_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,1,1,1),_MpWredIFStatPrecValue_Type())
mpWredIFStatPrecValue.setMaxAccess(_F)
if mibBuilder.loadTexts:mpWredIFStatPrecValue.setStatus(_A)
_MpWredIFStatRandomDropPkt64_Type=Counter64
_MpWredIFStatRandomDropPkt64_Object=MibTableColumn
mpWredIFStatRandomDropPkt64=_MpWredIFStatRandomDropPkt64_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,1,1,2),_MpWredIFStatRandomDropPkt64_Type())
mpWredIFStatRandomDropPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredIFStatRandomDropPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpWredIFStatRandomDropPkt64.setUnits(_E)
_MpWredIFStatTailDropPkt64_Type=Counter64
_MpWredIFStatTailDropPkt64_Object=MibTableColumn
mpWredIFStatTailDropPkt64=_MpWredIFStatTailDropPkt64_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,1,1,3),_MpWredIFStatTailDropPkt64_Type())
mpWredIFStatTailDropPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredIFStatTailDropPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpWredIFStatTailDropPkt64.setUnits(_E)
_MpWredIFStatTransmitPkt64_Type=Counter64
_MpWredIFStatTransmitPkt64_Object=MibTableColumn
mpWredIFStatTransmitPkt64=_MpWredIFStatTransmitPkt64_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,1,1,4),_MpWredIFStatTransmitPkt64_Type())
mpWredIFStatTransmitPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredIFStatTransmitPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpWredIFStatTransmitPkt64.setUnits(_E)
_MpWredFrameRelayVCStatTable_Object=MibTable
mpWredFrameRelayVCStatTable=_MpWredFrameRelayVCStatTable_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,2))
if mibBuilder.loadTexts:mpWredFrameRelayVCStatTable.setStatus(_A)
_MpWredFrameRelayVCStatEntry_Object=MibTableRow
mpWredFrameRelayVCStatEntry=_MpWredFrameRelayVCStatEntry_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,2,1))
mpWredFrameRelayVCStatEntry.setIndexNames((0,_C,_G),(0,_C,_R),(0,_C,_a))
if mibBuilder.loadTexts:mpWredFrameRelayVCStatEntry.setStatus(_A)
class _MpWredFRStatPrecValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_MpWredFRStatPrecValue_Type.__name__=_D
_MpWredFRStatPrecValue_Object=MibTableColumn
mpWredFRStatPrecValue=_MpWredFRStatPrecValue_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,2,1,1),_MpWredFRStatPrecValue_Type())
mpWredFRStatPrecValue.setMaxAccess(_F)
if mibBuilder.loadTexts:mpWredFRStatPrecValue.setStatus(_A)
_MpWredFRStatRandomDropPkt64_Type=Counter64
_MpWredFRStatRandomDropPkt64_Object=MibTableColumn
mpWredFRStatRandomDropPkt64=_MpWredFRStatRandomDropPkt64_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,2,1,2),_MpWredFRStatRandomDropPkt64_Type())
mpWredFRStatRandomDropPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredFRStatRandomDropPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpWredFRStatRandomDropPkt64.setUnits(_E)
_MpWredFRStatTailDropPkt64_Type=Counter64
_MpWredFRStatTailDropPkt64_Object=MibTableColumn
mpWredFRStatTailDropPkt64=_MpWredFRStatTailDropPkt64_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,2,1,3),_MpWredFRStatTailDropPkt64_Type())
mpWredFRStatTailDropPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredFRStatTailDropPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpWredFRStatTailDropPkt64.setUnits(_E)
_MpWredFRStatTransmitPkt64_Type=Counter64
_MpWredFRStatTransmitPkt64_Object=MibTableColumn
mpWredFRStatTransmitPkt64=_MpWredFRStatTransmitPkt64_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,2,1,4),_MpWredFRStatTransmitPkt64_Type())
mpWredFRStatTransmitPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredFRStatTransmitPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpWredFRStatTransmitPkt64.setUnits(_E)
_MpWredATMPVCStatTable_Object=MibTable
mpWredATMPVCStatTable=_MpWredATMPVCStatTable_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,3))
if mibBuilder.loadTexts:mpWredATMPVCStatTable.setStatus(_A)
_MpWredATMPVCStatEntry_Object=MibTableRow
mpWredATMPVCStatEntry=_MpWredATMPVCStatEntry_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,3,1))
mpWredATMPVCStatEntry.setIndexNames((0,_C,_G),(0,_C,_S),(0,_C,_T),(0,_C,_b))
if mibBuilder.loadTexts:mpWredATMPVCStatEntry.setStatus(_A)
class _MpWredATMStatPrecValue_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,63))
_MpWredATMStatPrecValue_Type.__name__=_D
_MpWredATMStatPrecValue_Object=MibTableColumn
mpWredATMStatPrecValue=_MpWredATMStatPrecValue_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,3,1,1),_MpWredATMStatPrecValue_Type())
mpWredATMStatPrecValue.setMaxAccess(_F)
if mibBuilder.loadTexts:mpWredATMStatPrecValue.setStatus(_A)
_MpWredATMStatRandomDropPkt64_Type=Counter64
_MpWredATMStatRandomDropPkt64_Object=MibTableColumn
mpWredATMStatRandomDropPkt64=_MpWredATMStatRandomDropPkt64_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,3,1,2),_MpWredATMStatRandomDropPkt64_Type())
mpWredATMStatRandomDropPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredATMStatRandomDropPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpWredATMStatRandomDropPkt64.setUnits(_E)
_MpWredATMStatTailDropPkt64_Type=Counter64
_MpWredATMStatTailDropPkt64_Object=MibTableColumn
mpWredATMStatTailDropPkt64=_MpWredATMStatTailDropPkt64_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,3,1,3),_MpWredATMStatTailDropPkt64_Type())
mpWredATMStatTailDropPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredATMStatTailDropPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpWredATMStatTailDropPkt64.setUnits(_E)
_MpWredATMStatTransmitPkt64_Type=Counter64
_MpWredATMStatTransmitPkt64_Object=MibTableColumn
mpWredATMStatTransmitPkt64=_MpWredATMStatTransmitPkt64_Object((1,3,6,1,4,1,5651,6,2,3,2,1,2,3,1,4),_MpWredATMStatTransmitPkt64_Type())
mpWredATMStatTransmitPkt64.setMaxAccess(_B)
if mibBuilder.loadTexts:mpWredATMStatTransmitPkt64.setStatus(_A)
if mibBuilder.loadTexts:mpWredATMStatTransmitPkt64.setUnits(_E)
mibBuilder.exportSymbols(_C,**{'maipu':maipu,'mpMgmt2':mpMgmt2,'mpRouterTech':mpRouterTech,'mpRtQoSv2':mpRtQoSv2,'maipuWredMIB':maipuWredMIB,'maipuWredMIBObjects':maipuWredMIBObjects,'mpWredConfig':mpWredConfig,'mpWredGroupCfgTable':mpWredGroupCfgTable,'mpWredGroupCfgEntry':mpWredGroupCfgEntry,_U:mpWredGroupCfgName,'mpWredGroupCfgDscpPrec':mpWredGroupCfgDscpPrec,'mpWredGroupCfgExponWeight':mpWredGroupCfgExponWeight,'mpWredGroupPrecCfgTable':mpWredGroupPrecCfgTable,'mpWredGroupPrecCfgEntry':mpWredGroupPrecCfgEntry,_V:mpWredGroupPrecCfgValue,'mpWredGroupPrecCfgMinThreshold':mpWredGroupPrecCfgMinThreshold,'mpWredGroupPrecCfgMaxThreshold':mpWredGroupPrecCfgMaxThreshold,'mpWredGroupPrecCfgPktDropProb':mpWredGroupPrecCfgPktDropProb,'mpWredInterfaceCfgTable':mpWredInterfaceCfgTable,'mpWredInterfaceCfgEntry':mpWredInterfaceCfgEntry,'mpWredIFCfgGroupName':mpWredIFCfgGroupName,'mpWredIFCfgDscpPrec':mpWredIFCfgDscpPrec,'mpWredIFCfgExponWeight':mpWredIFCfgExponWeight,'mpWredFrameRelayVCCfgTable':mpWredFrameRelayVCCfgTable,'mpWredFrameRelayVCCfgEntry':mpWredFrameRelayVCCfgEntry,_R:mpWredFRCfgDLCI,'mpWredFRCfgGroupName':mpWredFRCfgGroupName,'mpWredFRCfgDscpPrec':mpWredFRCfgDscpPrec,'mpWredFRCfgExponWeight':mpWredFRCfgExponWeight,'mpWredATMPVCCfgTable':mpWredATMPVCCfgTable,'mpWredATMPVCCfgEntry':mpWredATMPVCCfgEntry,_S:mpWredATMCfgVPI,_T:mpWredATMCfgVCI,'mpWredATMCfgGroupName':mpWredATMCfgGroupName,'mpWredATMCfgDscpPrec':mpWredATMCfgDscpPrec,'mpWredATMCfgExponWeight':mpWredATMCfgExponWeight,'mpWredCfgInterfacePrecTable':mpWredCfgInterfacePrecTable,'mpWredCfgInterfacePrecEntry':mpWredCfgInterfacePrecEntry,_W:mpWredIFPrecCfgValue,'mpWredIFPrecCfgMinThreshold':mpWredIFPrecCfgMinThreshold,'mpWredIFPrecCfgMaxThreshold':mpWredIFPrecCfgMaxThreshold,'mpWredIFPrecCfgPktDropProb':mpWredIFPrecCfgPktDropProb,'mpWredCfgFrameRelayVCPrecTable':mpWredCfgFrameRelayVCPrecTable,'mpWredCfgFrameRelayVCPrecEntry':mpWredCfgFrameRelayVCPrecEntry,_X:mpWredFRPrecCfgValue,'mpWredFRPrecCfgMinThreshold':mpWredFRPrecCfgMinThreshold,'mpWredFRPrecCfgMaxThreshold':mpWredFRPrecCfgMaxThreshold,'mpWredFRPrecCfgPktDropProb':mpWredFRPrecCfgPktDropProb,'mpWredCfgATMPVCPrecTable':mpWredCfgATMPVCPrecTable,'mpWredCfgATMPVCPrecEntry':mpWredCfgATMPVCPrecEntry,_Y:mpWredATMPrecCfgValue,'mpWredATMPrecCfgMinThreshold':mpWredATMPrecCfgMinThreshold,'mpWredATMPrecCfgMaxThreshold':mpWredATMPrecCfgMaxThreshold,'mpWredATMPrecCfgPktDropProb':mpWredATMPrecCfgPktDropProb,'mpWredStats':mpWredStats,'mpWredInterfaceStatTable':mpWredInterfaceStatTable,'mpWredInterfaceStatEntry':mpWredInterfaceStatEntry,_Z:mpWredIFStatPrecValue,'mpWredIFStatRandomDropPkt64':mpWredIFStatRandomDropPkt64,'mpWredIFStatTailDropPkt64':mpWredIFStatTailDropPkt64,'mpWredIFStatTransmitPkt64':mpWredIFStatTransmitPkt64,'mpWredFrameRelayVCStatTable':mpWredFrameRelayVCStatTable,'mpWredFrameRelayVCStatEntry':mpWredFrameRelayVCStatEntry,_a:mpWredFRStatPrecValue,'mpWredFRStatRandomDropPkt64':mpWredFRStatRandomDropPkt64,'mpWredFRStatTailDropPkt64':mpWredFRStatTailDropPkt64,'mpWredFRStatTransmitPkt64':mpWredFRStatTransmitPkt64,'mpWredATMPVCStatTable':mpWredATMPVCStatTable,'mpWredATMPVCStatEntry':mpWredATMPVCStatEntry,_b:mpWredATMStatPrecValue,'mpWredATMStatRandomDropPkt64':mpWredATMStatRandomDropPkt64,'mpWredATMStatTailDropPkt64':mpWredATMStatTailDropPkt64,'mpWredATMStatTransmitPkt64':mpWredATMStatTransmitPkt64})