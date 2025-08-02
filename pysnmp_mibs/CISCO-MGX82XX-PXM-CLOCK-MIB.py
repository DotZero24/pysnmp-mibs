_X='cmpExtClockInfoGroup'
_W='cmpSecondaryClockInfoGroup'
_V='cmpPrimaryClockInfoGroup'
_U='cmpClockInfoGroup'
_T='pxmExtClk2ConnectorType'
_S='pxmExtClk2SrcImpedance'
_R='pxmExtClock2Present'
_Q='pxmExtClkConnectorType'
_P='pxmExtClkSrcImpedance'
_O='pxmExtClockPresent'
_N='pxmSecondarySMClockSourceSlotNumber'
_M='pxmSecondaryInbandClockSourceLineNumber'
_L='pxmSecondaryMuxClockSource'
_K='pxmPrimarySMClockSourceSlotNumber'
_J='pxmPrimaryInbandClockSourceLineNumber'
_I='pxmPrimaryMuxClockSource'
_H='pxmClkErrReason'
_G='pxmClkStratumLevel'
_F='pxmPreviousClock'
_E='pxmCurrentClock'
_D='Integer32'
_C='read-only'
_B='CISCO-MGX82XX-PXM-CLOCK-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
cardSpecific,=mibBuilder.importSymbols('BASIS-MIB','cardSpecific')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
ciscoMgx82xxPxmClockMIB=ModuleIdentity((1,3,6,1,4,1,351,150,72))
if mibBuilder.loadTexts:ciscoMgx82xxPxmClockMIB.setRevisions(('2003-05-27 00:00',))
class CmpClockConnectorType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('rj45Type',1),('smbType',2)))
class CmpClockSourceType(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('pxmInbandClock1',1),('pxmServiceModuleClock1',2),('pxmTopSRMClock',3),('pxmExternalClock',4),('pxmInbandClock2',5),('pxmServiceModuleClock2',6),('pxmBottomSRMClock',7),('pxmInternalOscillator',8),('pxmExternalClock2',9)))
class CmpCurrentClock(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('primary',1),('secondary',2),('intOscillator',3)))
class CmpClockExistence(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('clkNotPresent',1),('clkPresent',2)))
class CmpClockImpedance(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ohms75',1),('ohms100',2),('ohms120',3)))
_PxmClockConfig_ObjectIdentity=ObjectIdentity
pxmClockConfig=_PxmClockConfig_ObjectIdentity((1,3,6,1,4,1,351,110,3,16))
_PxmPrimaryMuxClockSource_Type=CmpClockSourceType
_PxmPrimaryMuxClockSource_Object=MibScalar
pxmPrimaryMuxClockSource=_PxmPrimaryMuxClockSource_Object((1,3,6,1,4,1,351,110,3,16,1),_PxmPrimaryMuxClockSource_Type())
pxmPrimaryMuxClockSource.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmPrimaryMuxClockSource.setStatus(_A)
class _PxmPrimaryInbandClockSourceLineNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_PxmPrimaryInbandClockSourceLineNumber_Type.__name__=_D
_PxmPrimaryInbandClockSourceLineNumber_Object=MibScalar
pxmPrimaryInbandClockSourceLineNumber=_PxmPrimaryInbandClockSourceLineNumber_Object((1,3,6,1,4,1,351,110,3,16,2),_PxmPrimaryInbandClockSourceLineNumber_Type())
pxmPrimaryInbandClockSourceLineNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmPrimaryInbandClockSourceLineNumber.setStatus(_A)
class _PxmPrimarySMClockSourceSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_PxmPrimarySMClockSourceSlotNumber_Type.__name__=_D
_PxmPrimarySMClockSourceSlotNumber_Object=MibScalar
pxmPrimarySMClockSourceSlotNumber=_PxmPrimarySMClockSourceSlotNumber_Object((1,3,6,1,4,1,351,110,3,16,3),_PxmPrimarySMClockSourceSlotNumber_Type())
pxmPrimarySMClockSourceSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmPrimarySMClockSourceSlotNumber.setStatus(_A)
_PxmSecondaryMuxClockSource_Type=CmpClockSourceType
_PxmSecondaryMuxClockSource_Object=MibScalar
pxmSecondaryMuxClockSource=_PxmSecondaryMuxClockSource_Object((1,3,6,1,4,1,351,110,3,16,4),_PxmSecondaryMuxClockSource_Type())
pxmSecondaryMuxClockSource.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmSecondaryMuxClockSource.setStatus(_A)
class _PxmSecondaryInbandClockSourceLineNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,4))
_PxmSecondaryInbandClockSourceLineNumber_Type.__name__=_D
_PxmSecondaryInbandClockSourceLineNumber_Object=MibScalar
pxmSecondaryInbandClockSourceLineNumber=_PxmSecondaryInbandClockSourceLineNumber_Object((1,3,6,1,4,1,351,110,3,16,5),_PxmSecondaryInbandClockSourceLineNumber_Type())
pxmSecondaryInbandClockSourceLineNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmSecondaryInbandClockSourceLineNumber.setStatus(_A)
class _PxmSecondarySMClockSourceSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,32))
_PxmSecondarySMClockSourceSlotNumber_Type.__name__=_D
_PxmSecondarySMClockSourceSlotNumber_Object=MibScalar
pxmSecondarySMClockSourceSlotNumber=_PxmSecondarySMClockSourceSlotNumber_Object((1,3,6,1,4,1,351,110,3,16,6),_PxmSecondarySMClockSourceSlotNumber_Type())
pxmSecondarySMClockSourceSlotNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmSecondarySMClockSourceSlotNumber.setStatus(_A)
_PxmCurrentClock_Type=CmpCurrentClock
_PxmCurrentClock_Object=MibScalar
pxmCurrentClock=_PxmCurrentClock_Object((1,3,6,1,4,1,351,110,3,16,7),_PxmCurrentClock_Type())
pxmCurrentClock.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmCurrentClock.setStatus(_A)
_PxmPreviousClock_Type=CmpCurrentClock
_PxmPreviousClock_Object=MibScalar
pxmPreviousClock=_PxmPreviousClock_Object((1,3,6,1,4,1,351,110,3,16,8),_PxmPreviousClock_Type())
pxmPreviousClock.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmPreviousClock.setStatus(_A)
_PxmExtClockPresent_Type=CmpClockExistence
_PxmExtClockPresent_Object=MibScalar
pxmExtClockPresent=_PxmExtClockPresent_Object((1,3,6,1,4,1,351,110,3,16,9),_PxmExtClockPresent_Type())
pxmExtClockPresent.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmExtClockPresent.setStatus(_A)
_PxmExtClkSrcImpedance_Type=CmpClockImpedance
_PxmExtClkSrcImpedance_Object=MibScalar
pxmExtClkSrcImpedance=_PxmExtClkSrcImpedance_Object((1,3,6,1,4,1,351,110,3,16,10),_PxmExtClkSrcImpedance_Type())
pxmExtClkSrcImpedance.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmExtClkSrcImpedance.setStatus(_A)
_PxmExtClkConnectorType_Type=CmpClockConnectorType
_PxmExtClkConnectorType_Object=MibScalar
pxmExtClkConnectorType=_PxmExtClkConnectorType_Object((1,3,6,1,4,1,351,110,3,16,11),_PxmExtClkConnectorType_Type())
pxmExtClkConnectorType.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmExtClkConnectorType.setStatus(_A)
class _PxmClkStratumLevel_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('stratumUnknown',1),('stratumLevel1',2),('stratumLevel2',3),('stratumLevel3E',4),('stratumLevel3',5),('stratumLevel4',6),('stratumLevel4E',7)))
_PxmClkStratumLevel_Type.__name__=_D
_PxmClkStratumLevel_Object=MibScalar
pxmClkStratumLevel=_PxmClkStratumLevel_Object((1,3,6,1,4,1,351,110,3,16,12),_PxmClkStratumLevel_Type())
pxmClkStratumLevel.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmClkStratumLevel.setStatus(_A)
class _PxmClkErrReason_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('goodClk',1),('unknownReason',2),('noClkSignal',3),('freqTooHigh',4),('freqTooLow',5),('excessiveJitter',6),('missingCard',7),('missingLogicalIf',8),('noClock',9)))
_PxmClkErrReason_Type.__name__=_D
_PxmClkErrReason_Object=MibScalar
pxmClkErrReason=_PxmClkErrReason_Object((1,3,6,1,4,1,351,110,3,16,13),_PxmClkErrReason_Type())
pxmClkErrReason.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmClkErrReason.setStatus(_A)
_PxmExtClock2Present_Type=CmpClockExistence
_PxmExtClock2Present_Object=MibScalar
pxmExtClock2Present=_PxmExtClock2Present_Object((1,3,6,1,4,1,351,110,3,16,14),_PxmExtClock2Present_Type())
pxmExtClock2Present.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmExtClock2Present.setStatus(_A)
_PxmExtClk2SrcImpedance_Type=CmpClockImpedance
_PxmExtClk2SrcImpedance_Object=MibScalar
pxmExtClk2SrcImpedance=_PxmExtClk2SrcImpedance_Object((1,3,6,1,4,1,351,110,3,16,15),_PxmExtClk2SrcImpedance_Type())
pxmExtClk2SrcImpedance.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmExtClk2SrcImpedance.setStatus(_A)
_PxmExtClk2ConnectorType_Type=CmpClockConnectorType
_PxmExtClk2ConnectorType_Object=MibScalar
pxmExtClk2ConnectorType=_PxmExtClk2ConnectorType_Object((1,3,6,1,4,1,351,110,3,16,16),_PxmExtClk2ConnectorType_Type())
pxmExtClk2ConnectorType.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmExtClk2ConnectorType.setStatus(_A)
_CmpClockMIBConformance_ObjectIdentity=ObjectIdentity
cmpClockMIBConformance=_CmpClockMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,72,2))
_CmpClockMIBGroups_ObjectIdentity=ObjectIdentity
cmpClockMIBGroups=_CmpClockMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,72,2,1))
_CmpClockMIBCompliances_ObjectIdentity=ObjectIdentity
cmpClockMIBCompliances=_CmpClockMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,72,2,2))
cmpClockInfoGroup=ObjectGroup((1,3,6,1,4,1,351,150,72,2,1,1))
cmpClockInfoGroup.setObjects(*((_B,_E),(_B,_F),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:cmpClockInfoGroup.setStatus(_A)
cmpPrimaryClockInfoGroup=ObjectGroup((1,3,6,1,4,1,351,150,72,2,1,2))
cmpPrimaryClockInfoGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:cmpPrimaryClockInfoGroup.setStatus(_A)
cmpSecondaryClockInfoGroup=ObjectGroup((1,3,6,1,4,1,351,150,72,2,1,3))
cmpSecondaryClockInfoGroup.setObjects(*((_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:cmpSecondaryClockInfoGroup.setStatus(_A)
cmpExtClockInfoGroup=ObjectGroup((1,3,6,1,4,1,351,150,72,2,1,4))
cmpExtClockInfoGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:cmpExtClockInfoGroup.setStatus(_A)
cmpClockCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,72,2,2,1))
cmpClockCompliance.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X)))
if mibBuilder.loadTexts:cmpClockCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'CmpClockConnectorType':CmpClockConnectorType,'CmpClockSourceType':CmpClockSourceType,'CmpCurrentClock':CmpCurrentClock,'CmpClockExistence':CmpClockExistence,'CmpClockImpedance':CmpClockImpedance,'pxmClockConfig':pxmClockConfig,_I:pxmPrimaryMuxClockSource,_J:pxmPrimaryInbandClockSourceLineNumber,_K:pxmPrimarySMClockSourceSlotNumber,_L:pxmSecondaryMuxClockSource,_M:pxmSecondaryInbandClockSourceLineNumber,_N:pxmSecondarySMClockSourceSlotNumber,_E:pxmCurrentClock,_F:pxmPreviousClock,_O:pxmExtClockPresent,_P:pxmExtClkSrcImpedance,_Q:pxmExtClkConnectorType,_G:pxmClkStratumLevel,_H:pxmClkErrReason,_R:pxmExtClock2Present,_S:pxmExtClk2SrcImpedance,_T:pxmExtClk2ConnectorType,'ciscoMgx82xxPxmClockMIB':ciscoMgx82xxPxmClockMIB,'cmpClockMIBConformance':cmpClockMIBConformance,'cmpClockMIBGroups':cmpClockMIBGroups,_U:cmpClockInfoGroup,_V:cmpPrimaryClockInfoGroup,_W:cmpSecondaryClockInfoGroup,_X:cmpExtClockInfoGroup,'cmpClockMIBCompliances':cmpClockMIBCompliances,'cmpClockCompliance':cmpClockCompliance})