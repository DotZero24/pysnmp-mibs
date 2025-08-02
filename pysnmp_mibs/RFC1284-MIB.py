_K='dot3CollCount'
_J='dot3CollIndex'
_I='dot3StatsIndex'
_H='disabled'
_G='enabled'
_F='dot3Index'
_E='read-write'
_D='RFC1284-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,transmission=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','transmission')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Dot3_ObjectIdentity=ObjectIdentity
dot3=_Dot3_ObjectIdentity((1,3,6,1,2,1,10,7))
_Dot3Table_Object=MibTable
dot3Table=_Dot3Table_Object((1,3,6,1,2,1,10,7,1))
if mibBuilder.loadTexts:dot3Table.setStatus(_A)
_Dot3Entry_Object=MibTableRow
dot3Entry=_Dot3Entry_Object((1,3,6,1,2,1,10,7,1,1))
dot3Entry.setIndexNames((0,_D,_F))
if mibBuilder.loadTexts:dot3Entry.setStatus(_A)
_Dot3Index_Type=Integer32
_Dot3Index_Object=MibTableColumn
dot3Index=_Dot3Index_Object((1,3,6,1,2,1,10,7,1,1,1),_Dot3Index_Type())
dot3Index.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3Index.setStatus(_A)
class _Dot3InitializeMac_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('initialized',1),('uninitialized',2)))
_Dot3InitializeMac_Type.__name__=_C
_Dot3InitializeMac_Object=MibTableColumn
dot3InitializeMac=_Dot3InitializeMac_Object((1,3,6,1,2,1,10,7,1,1,2),_Dot3InitializeMac_Type())
dot3InitializeMac.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3InitializeMac.setStatus(_A)
class _Dot3MacSubLayerStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Dot3MacSubLayerStatus_Type.__name__=_C
_Dot3MacSubLayerStatus_Object=MibTableColumn
dot3MacSubLayerStatus=_Dot3MacSubLayerStatus_Object((1,3,6,1,2,1,10,7,1,1,3),_Dot3MacSubLayerStatus_Type())
dot3MacSubLayerStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3MacSubLayerStatus.setStatus(_A)
class _Dot3MulticastReceiveStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_G,1),(_H,2)))
_Dot3MulticastReceiveStatus_Type.__name__=_C
_Dot3MulticastReceiveStatus_Object=MibTableColumn
dot3MulticastReceiveStatus=_Dot3MulticastReceiveStatus_Object((1,3,6,1,2,1,10,7,1,1,4),_Dot3MulticastReceiveStatus_Type())
dot3MulticastReceiveStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3MulticastReceiveStatus.setStatus(_A)
class _Dot3TxEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Dot3TxEnabled_Type.__name__=_C
_Dot3TxEnabled_Object=MibTableColumn
dot3TxEnabled=_Dot3TxEnabled_Object((1,3,6,1,2,1,10,7,1,1,5),_Dot3TxEnabled_Type())
dot3TxEnabled.setMaxAccess(_E)
if mibBuilder.loadTexts:dot3TxEnabled.setStatus(_A)
_Dot3TestTdrValue_Type=Gauge32
_Dot3TestTdrValue_Object=MibTableColumn
dot3TestTdrValue=_Dot3TestTdrValue_Object((1,3,6,1,2,1,10,7,1,1,6),_Dot3TestTdrValue_Type())
dot3TestTdrValue.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3TestTdrValue.setStatus(_A)
_Dot3StatsTable_Object=MibTable
dot3StatsTable=_Dot3StatsTable_Object((1,3,6,1,2,1,10,7,2))
if mibBuilder.loadTexts:dot3StatsTable.setStatus(_A)
_Dot3StatsEntry_Object=MibTableRow
dot3StatsEntry=_Dot3StatsEntry_Object((1,3,6,1,2,1,10,7,2,1))
dot3StatsEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:dot3StatsEntry.setStatus(_A)
_Dot3StatsIndex_Type=Integer32
_Dot3StatsIndex_Object=MibTableColumn
dot3StatsIndex=_Dot3StatsIndex_Object((1,3,6,1,2,1,10,7,2,1,1),_Dot3StatsIndex_Type())
dot3StatsIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3StatsIndex.setStatus(_A)
_Dot3StatsAlignmentErrors_Type=Counter32
_Dot3StatsAlignmentErrors_Object=MibTableColumn
dot3StatsAlignmentErrors=_Dot3StatsAlignmentErrors_Object((1,3,6,1,2,1,10,7,2,1,2),_Dot3StatsAlignmentErrors_Type())
dot3StatsAlignmentErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3StatsAlignmentErrors.setStatus(_A)
_Dot3StatsFCSErrors_Type=Counter32
_Dot3StatsFCSErrors_Object=MibTableColumn
dot3StatsFCSErrors=_Dot3StatsFCSErrors_Object((1,3,6,1,2,1,10,7,2,1,3),_Dot3StatsFCSErrors_Type())
dot3StatsFCSErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3StatsFCSErrors.setStatus(_A)
_Dot3StatsSingleCollisionFrames_Type=Counter32
_Dot3StatsSingleCollisionFrames_Object=MibTableColumn
dot3StatsSingleCollisionFrames=_Dot3StatsSingleCollisionFrames_Object((1,3,6,1,2,1,10,7,2,1,4),_Dot3StatsSingleCollisionFrames_Type())
dot3StatsSingleCollisionFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3StatsSingleCollisionFrames.setStatus(_A)
_Dot3StatsMultipleCollisionFrames_Type=Counter32
_Dot3StatsMultipleCollisionFrames_Object=MibTableColumn
dot3StatsMultipleCollisionFrames=_Dot3StatsMultipleCollisionFrames_Object((1,3,6,1,2,1,10,7,2,1,5),_Dot3StatsMultipleCollisionFrames_Type())
dot3StatsMultipleCollisionFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3StatsMultipleCollisionFrames.setStatus(_A)
_Dot3StatsSQETestErrors_Type=Counter32
_Dot3StatsSQETestErrors_Object=MibTableColumn
dot3StatsSQETestErrors=_Dot3StatsSQETestErrors_Object((1,3,6,1,2,1,10,7,2,1,6),_Dot3StatsSQETestErrors_Type())
dot3StatsSQETestErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3StatsSQETestErrors.setStatus(_A)
_Dot3StatsDeferredTransmissions_Type=Counter32
_Dot3StatsDeferredTransmissions_Object=MibTableColumn
dot3StatsDeferredTransmissions=_Dot3StatsDeferredTransmissions_Object((1,3,6,1,2,1,10,7,2,1,7),_Dot3StatsDeferredTransmissions_Type())
dot3StatsDeferredTransmissions.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3StatsDeferredTransmissions.setStatus(_A)
_Dot3StatsLateCollisions_Type=Counter32
_Dot3StatsLateCollisions_Object=MibTableColumn
dot3StatsLateCollisions=_Dot3StatsLateCollisions_Object((1,3,6,1,2,1,10,7,2,1,8),_Dot3StatsLateCollisions_Type())
dot3StatsLateCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3StatsLateCollisions.setStatus(_A)
_Dot3StatsExcessiveCollisions_Type=Counter32
_Dot3StatsExcessiveCollisions_Object=MibTableColumn
dot3StatsExcessiveCollisions=_Dot3StatsExcessiveCollisions_Object((1,3,6,1,2,1,10,7,2,1,9),_Dot3StatsExcessiveCollisions_Type())
dot3StatsExcessiveCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3StatsExcessiveCollisions.setStatus(_A)
_Dot3StatsInternalMacTransmitErrors_Type=Counter32
_Dot3StatsInternalMacTransmitErrors_Object=MibTableColumn
dot3StatsInternalMacTransmitErrors=_Dot3StatsInternalMacTransmitErrors_Object((1,3,6,1,2,1,10,7,2,1,10),_Dot3StatsInternalMacTransmitErrors_Type())
dot3StatsInternalMacTransmitErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3StatsInternalMacTransmitErrors.setStatus(_A)
_Dot3StatsCarrierSenseErrors_Type=Counter32
_Dot3StatsCarrierSenseErrors_Object=MibTableColumn
dot3StatsCarrierSenseErrors=_Dot3StatsCarrierSenseErrors_Object((1,3,6,1,2,1,10,7,2,1,11),_Dot3StatsCarrierSenseErrors_Type())
dot3StatsCarrierSenseErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3StatsCarrierSenseErrors.setStatus(_A)
_Dot3StatsExcessiveDeferrals_Type=Counter32
_Dot3StatsExcessiveDeferrals_Object=MibTableColumn
dot3StatsExcessiveDeferrals=_Dot3StatsExcessiveDeferrals_Object((1,3,6,1,2,1,10,7,2,1,12),_Dot3StatsExcessiveDeferrals_Type())
dot3StatsExcessiveDeferrals.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3StatsExcessiveDeferrals.setStatus(_A)
_Dot3StatsFrameTooLongs_Type=Counter32
_Dot3StatsFrameTooLongs_Object=MibTableColumn
dot3StatsFrameTooLongs=_Dot3StatsFrameTooLongs_Object((1,3,6,1,2,1,10,7,2,1,13),_Dot3StatsFrameTooLongs_Type())
dot3StatsFrameTooLongs.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3StatsFrameTooLongs.setStatus(_A)
_Dot3StatsInRangeLengthErrors_Type=Counter32
_Dot3StatsInRangeLengthErrors_Object=MibTableColumn
dot3StatsInRangeLengthErrors=_Dot3StatsInRangeLengthErrors_Object((1,3,6,1,2,1,10,7,2,1,14),_Dot3StatsInRangeLengthErrors_Type())
dot3StatsInRangeLengthErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3StatsInRangeLengthErrors.setStatus(_A)
_Dot3StatsOutOfRangeLengthFields_Type=Counter32
_Dot3StatsOutOfRangeLengthFields_Object=MibTableColumn
dot3StatsOutOfRangeLengthFields=_Dot3StatsOutOfRangeLengthFields_Object((1,3,6,1,2,1,10,7,2,1,15),_Dot3StatsOutOfRangeLengthFields_Type())
dot3StatsOutOfRangeLengthFields.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3StatsOutOfRangeLengthFields.setStatus(_A)
_Dot3StatsInternalMacReceiveErrors_Type=Counter32
_Dot3StatsInternalMacReceiveErrors_Object=MibTableColumn
dot3StatsInternalMacReceiveErrors=_Dot3StatsInternalMacReceiveErrors_Object((1,3,6,1,2,1,10,7,2,1,16),_Dot3StatsInternalMacReceiveErrors_Type())
dot3StatsInternalMacReceiveErrors.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3StatsInternalMacReceiveErrors.setStatus(_A)
_Dot3CollTable_Object=MibTable
dot3CollTable=_Dot3CollTable_Object((1,3,6,1,2,1,10,7,5))
if mibBuilder.loadTexts:dot3CollTable.setStatus(_A)
_Dot3CollEntry_Object=MibTableRow
dot3CollEntry=_Dot3CollEntry_Object((1,3,6,1,2,1,10,7,5,1))
dot3CollEntry.setIndexNames((0,_D,_J),(0,_D,_K))
if mibBuilder.loadTexts:dot3CollEntry.setStatus(_A)
_Dot3CollIndex_Type=Integer32
_Dot3CollIndex_Object=MibTableColumn
dot3CollIndex=_Dot3CollIndex_Object((1,3,6,1,2,1,10,7,5,1,1),_Dot3CollIndex_Type())
dot3CollIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3CollIndex.setStatus(_A)
class _Dot3CollCount_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_Dot3CollCount_Type.__name__=_C
_Dot3CollCount_Object=MibTableColumn
dot3CollCount=_Dot3CollCount_Object((1,3,6,1,2,1,10,7,5,1,2),_Dot3CollCount_Type())
dot3CollCount.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3CollCount.setStatus(_A)
_Dot3CollFrequencies_Type=Counter32
_Dot3CollFrequencies_Object=MibTableColumn
dot3CollFrequencies=_Dot3CollFrequencies_Object((1,3,6,1,2,1,10,7,5,1,3),_Dot3CollFrequencies_Type())
dot3CollFrequencies.setMaxAccess(_B)
if mibBuilder.loadTexts:dot3CollFrequencies.setStatus(_A)
_Dot3Tests_ObjectIdentity=ObjectIdentity
dot3Tests=_Dot3Tests_ObjectIdentity((1,3,6,1,2,1,10,7,6))
_Dot3TestTdr_ObjectIdentity=ObjectIdentity
dot3TestTdr=_Dot3TestTdr_ObjectIdentity((1,3,6,1,2,1,10,7,6,1))
_Dot3Errors_ObjectIdentity=ObjectIdentity
dot3Errors=_Dot3Errors_ObjectIdentity((1,3,6,1,2,1,10,7,7))
_Dot3ErrorInitError_ObjectIdentity=ObjectIdentity
dot3ErrorInitError=_Dot3ErrorInitError_ObjectIdentity((1,3,6,1,2,1,10,7,7,1))
_Dot3ErrorLoopbackError_ObjectIdentity=ObjectIdentity
dot3ErrorLoopbackError=_Dot3ErrorLoopbackError_ObjectIdentity((1,3,6,1,2,1,10,7,7,2))
_Dot3ChipSets_ObjectIdentity=ObjectIdentity
dot3ChipSets=_Dot3ChipSets_ObjectIdentity((1,3,6,1,2,1,10,7,8))
_Dot3ChipSetAMD_ObjectIdentity=ObjectIdentity
dot3ChipSetAMD=_Dot3ChipSetAMD_ObjectIdentity((1,3,6,1,2,1,10,7,8,1))
_Dot3ChipSetAMD7990_ObjectIdentity=ObjectIdentity
dot3ChipSetAMD7990=_Dot3ChipSetAMD7990_ObjectIdentity((1,3,6,1,2,1,10,7,8,1,1))
_Dot3ChipSetAMD79900_ObjectIdentity=ObjectIdentity
dot3ChipSetAMD79900=_Dot3ChipSetAMD79900_ObjectIdentity((1,3,6,1,2,1,10,7,8,1,2))
_Dot3ChipSetIntel_ObjectIdentity=ObjectIdentity
dot3ChipSetIntel=_Dot3ChipSetIntel_ObjectIdentity((1,3,6,1,2,1,10,7,8,2))
_Dot3ChipSetIntel82586_ObjectIdentity=ObjectIdentity
dot3ChipSetIntel82586=_Dot3ChipSetIntel82586_ObjectIdentity((1,3,6,1,2,1,10,7,8,2,1))
_Dot3ChipSetIntel82596_ObjectIdentity=ObjectIdentity
dot3ChipSetIntel82596=_Dot3ChipSetIntel82596_ObjectIdentity((1,3,6,1,2,1,10,7,8,2,2))
_Dot3ChipSetSeeq_ObjectIdentity=ObjectIdentity
dot3ChipSetSeeq=_Dot3ChipSetSeeq_ObjectIdentity((1,3,6,1,2,1,10,7,8,3))
_Dot3ChipSetSeeq8003_ObjectIdentity=ObjectIdentity
dot3ChipSetSeeq8003=_Dot3ChipSetSeeq8003_ObjectIdentity((1,3,6,1,2,1,10,7,8,3,1))
_Dot3ChipSetNational_ObjectIdentity=ObjectIdentity
dot3ChipSetNational=_Dot3ChipSetNational_ObjectIdentity((1,3,6,1,2,1,10,7,8,4))
_Dot3ChipSetNational8390_ObjectIdentity=ObjectIdentity
dot3ChipSetNational8390=_Dot3ChipSetNational8390_ObjectIdentity((1,3,6,1,2,1,10,7,8,4,1))
_Dot3ChipSetNationalSonic_ObjectIdentity=ObjectIdentity
dot3ChipSetNationalSonic=_Dot3ChipSetNationalSonic_ObjectIdentity((1,3,6,1,2,1,10,7,8,4,2))
_Dot3ChipSetFujitsu_ObjectIdentity=ObjectIdentity
dot3ChipSetFujitsu=_Dot3ChipSetFujitsu_ObjectIdentity((1,3,6,1,2,1,10,7,8,5))
_Dot3ChipSetFujitsu86950_ObjectIdentity=ObjectIdentity
dot3ChipSetFujitsu86950=_Dot3ChipSetFujitsu86950_ObjectIdentity((1,3,6,1,2,1,10,7,8,5,1))
mibBuilder.exportSymbols(_D,**{'dot3':dot3,'dot3Table':dot3Table,'dot3Entry':dot3Entry,_F:dot3Index,'dot3InitializeMac':dot3InitializeMac,'dot3MacSubLayerStatus':dot3MacSubLayerStatus,'dot3MulticastReceiveStatus':dot3MulticastReceiveStatus,'dot3TxEnabled':dot3TxEnabled,'dot3TestTdrValue':dot3TestTdrValue,'dot3StatsTable':dot3StatsTable,'dot3StatsEntry':dot3StatsEntry,_I:dot3StatsIndex,'dot3StatsAlignmentErrors':dot3StatsAlignmentErrors,'dot3StatsFCSErrors':dot3StatsFCSErrors,'dot3StatsSingleCollisionFrames':dot3StatsSingleCollisionFrames,'dot3StatsMultipleCollisionFrames':dot3StatsMultipleCollisionFrames,'dot3StatsSQETestErrors':dot3StatsSQETestErrors,'dot3StatsDeferredTransmissions':dot3StatsDeferredTransmissions,'dot3StatsLateCollisions':dot3StatsLateCollisions,'dot3StatsExcessiveCollisions':dot3StatsExcessiveCollisions,'dot3StatsInternalMacTransmitErrors':dot3StatsInternalMacTransmitErrors,'dot3StatsCarrierSenseErrors':dot3StatsCarrierSenseErrors,'dot3StatsExcessiveDeferrals':dot3StatsExcessiveDeferrals,'dot3StatsFrameTooLongs':dot3StatsFrameTooLongs,'dot3StatsInRangeLengthErrors':dot3StatsInRangeLengthErrors,'dot3StatsOutOfRangeLengthFields':dot3StatsOutOfRangeLengthFields,'dot3StatsInternalMacReceiveErrors':dot3StatsInternalMacReceiveErrors,'dot3CollTable':dot3CollTable,'dot3CollEntry':dot3CollEntry,_J:dot3CollIndex,_K:dot3CollCount,'dot3CollFrequencies':dot3CollFrequencies,'dot3Tests':dot3Tests,'dot3TestTdr':dot3TestTdr,'dot3Errors':dot3Errors,'dot3ErrorInitError':dot3ErrorInitError,'dot3ErrorLoopbackError':dot3ErrorLoopbackError,'dot3ChipSets':dot3ChipSets,'dot3ChipSetAMD':dot3ChipSetAMD,'dot3ChipSetAMD7990':dot3ChipSetAMD7990,'dot3ChipSetAMD79900':dot3ChipSetAMD79900,'dot3ChipSetIntel':dot3ChipSetIntel,'dot3ChipSetIntel82586':dot3ChipSetIntel82586,'dot3ChipSetIntel82596':dot3ChipSetIntel82596,'dot3ChipSetSeeq':dot3ChipSetSeeq,'dot3ChipSetSeeq8003':dot3ChipSetSeeq8003,'dot3ChipSetNational':dot3ChipSetNational,'dot3ChipSetNational8390':dot3ChipSetNational8390,'dot3ChipSetNationalSonic':dot3ChipSetNationalSonic,'dot3ChipSetFujitsu':dot3ChipSetFujitsu,'dot3ChipSetFujitsu86950':dot3ChipSetFujitsu86950})