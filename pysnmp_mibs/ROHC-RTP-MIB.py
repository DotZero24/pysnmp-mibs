_e='rohcRtpStatisticsGroup'
_d='rohcRtpPacketSizesGroup'
_c='rohcRtpContextGroup'
_b='rohcRtpContextPktsLostPreLink'
_a='rohcRtpContextPktsLostPhysical'
_Z='rohcRtpContextCCPs'
_Y='rohcRtpContextCSPs'
_X='rohcRtpContextNHPs'
_W='rohcRtpContextSNACKs'
_V='rohcRtpContextNACKs'
_U='rohcRtpContextACKs'
_T='rohcRtpPacketSizeRestrictedType'
_S='rohcRtpPacketSizeUsed'
_R='rohcRtpPacketSizePreferred'
_Q='rohcRtpContextSizesUsed'
_P='rohcRtpContextSizesAllowed'
_O='rohcRtpContextVerifyPeriod'
_N='rohcRtpContextLargePktsAllowed'
_M='rohcRtpContextAlwaysPad'
_L='rohcRtpContextMode'
_K='rohcRtpContextState'
_J='rohcRtpPacketSize'
_I='TruthValue'
_H='rohcContextCID'
_G='rohcChannelID'
_F='Integer32'
_E='Unsigned32'
_D='ROHC-MIB'
_C='read-only'
_B='ROHC-RTP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rohcChannelID,rohcContextCID=mibBuilder.importSymbols(_D,_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso','mib-2')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_I)
rohcRtpMIB=ModuleIdentity((1,3,6,1,2,1,114))
if mibBuilder.loadTexts:rohcRtpMIB.setRevisions(('2004-06-03 00:00',))
_RohcRtpObjects_ObjectIdentity=ObjectIdentity
rohcRtpObjects=_RohcRtpObjects_ObjectIdentity((1,3,6,1,2,1,114,1))
_RohcRtpContextTable_Object=MibTable
rohcRtpContextTable=_RohcRtpContextTable_Object((1,3,6,1,2,1,114,1,1))
if mibBuilder.loadTexts:rohcRtpContextTable.setStatus(_A)
_RohcRtpContextEntry_Object=MibTableRow
rohcRtpContextEntry=_RohcRtpContextEntry_Object((1,3,6,1,2,1,114,1,1,1))
rohcRtpContextEntry.setIndexNames((0,_D,_G),(0,_D,_H))
if mibBuilder.loadTexts:rohcRtpContextEntry.setStatus(_A)
class _RohcRtpContextState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('initAndRefresh',1),('firstOrder',2),('secondOrder',3),('noContext',4),('staticContext',5),('fullContext',6)))
_RohcRtpContextState_Type.__name__=_F
_RohcRtpContextState_Object=MibTableColumn
rohcRtpContextState=_RohcRtpContextState_Object((1,3,6,1,2,1,114,1,1,1,3),_RohcRtpContextState_Type())
rohcRtpContextState.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpContextState.setStatus(_A)
class _RohcRtpContextMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unidirectional',1),('optimistic',2),('reliable',3)))
_RohcRtpContextMode_Type.__name__=_F
_RohcRtpContextMode_Object=MibTableColumn
rohcRtpContextMode=_RohcRtpContextMode_Object((1,3,6,1,2,1,114,1,1,1,4),_RohcRtpContextMode_Type())
rohcRtpContextMode.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpContextMode.setStatus(_A)
class _RohcRtpContextAlwaysPad_Type(TruthValue):defaultValue=2
_RohcRtpContextAlwaysPad_Type.__name__=_I
_RohcRtpContextAlwaysPad_Object=MibTableColumn
rohcRtpContextAlwaysPad=_RohcRtpContextAlwaysPad_Object((1,3,6,1,2,1,114,1,1,1,5),_RohcRtpContextAlwaysPad_Type())
rohcRtpContextAlwaysPad.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpContextAlwaysPad.setStatus(_A)
class _RohcRtpContextLargePktsAllowed_Type(TruthValue):defaultValue=1
_RohcRtpContextLargePktsAllowed_Type.__name__=_I
_RohcRtpContextLargePktsAllowed_Object=MibTableColumn
rohcRtpContextLargePktsAllowed=_RohcRtpContextLargePktsAllowed_Object((1,3,6,1,2,1,114,1,1,1,6),_RohcRtpContextLargePktsAllowed_Type())
rohcRtpContextLargePktsAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpContextLargePktsAllowed.setStatus(_A)
class _RohcRtpContextVerifyPeriod_Type(Unsigned32):defaultValue=0
_RohcRtpContextVerifyPeriod_Type.__name__=_E
_RohcRtpContextVerifyPeriod_Object=MibTableColumn
rohcRtpContextVerifyPeriod=_RohcRtpContextVerifyPeriod_Object((1,3,6,1,2,1,114,1,1,1,7),_RohcRtpContextVerifyPeriod_Type())
rohcRtpContextVerifyPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpContextVerifyPeriod.setStatus(_A)
class _RohcRtpContextSizesAllowed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RohcRtpContextSizesAllowed_Type.__name__=_E
_RohcRtpContextSizesAllowed_Object=MibTableColumn
rohcRtpContextSizesAllowed=_RohcRtpContextSizesAllowed_Object((1,3,6,1,2,1,114,1,1,1,8),_RohcRtpContextSizesAllowed_Type())
rohcRtpContextSizesAllowed.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpContextSizesAllowed.setStatus(_A)
class _RohcRtpContextSizesUsed_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RohcRtpContextSizesUsed_Type.__name__=_E
_RohcRtpContextSizesUsed_Object=MibTableColumn
rohcRtpContextSizesUsed=_RohcRtpContextSizesUsed_Object((1,3,6,1,2,1,114,1,1,1,9),_RohcRtpContextSizesUsed_Type())
rohcRtpContextSizesUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpContextSizesUsed.setStatus(_A)
_RohcRtpContextACKs_Type=Counter32
_RohcRtpContextACKs_Object=MibTableColumn
rohcRtpContextACKs=_RohcRtpContextACKs_Object((1,3,6,1,2,1,114,1,1,1,10),_RohcRtpContextACKs_Type())
rohcRtpContextACKs.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpContextACKs.setStatus(_A)
_RohcRtpContextNACKs_Type=Counter32
_RohcRtpContextNACKs_Object=MibTableColumn
rohcRtpContextNACKs=_RohcRtpContextNACKs_Object((1,3,6,1,2,1,114,1,1,1,11),_RohcRtpContextNACKs_Type())
rohcRtpContextNACKs.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpContextNACKs.setStatus(_A)
_RohcRtpContextSNACKs_Type=Counter32
_RohcRtpContextSNACKs_Object=MibTableColumn
rohcRtpContextSNACKs=_RohcRtpContextSNACKs_Object((1,3,6,1,2,1,114,1,1,1,12),_RohcRtpContextSNACKs_Type())
rohcRtpContextSNACKs.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpContextSNACKs.setStatus(_A)
_RohcRtpContextNHPs_Type=Counter32
_RohcRtpContextNHPs_Object=MibTableColumn
rohcRtpContextNHPs=_RohcRtpContextNHPs_Object((1,3,6,1,2,1,114,1,1,1,13),_RohcRtpContextNHPs_Type())
rohcRtpContextNHPs.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpContextNHPs.setStatus(_A)
_RohcRtpContextCSPs_Type=Counter32
_RohcRtpContextCSPs_Object=MibTableColumn
rohcRtpContextCSPs=_RohcRtpContextCSPs_Object((1,3,6,1,2,1,114,1,1,1,14),_RohcRtpContextCSPs_Type())
rohcRtpContextCSPs.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpContextCSPs.setStatus(_A)
_RohcRtpContextCCPs_Type=Counter32
_RohcRtpContextCCPs_Object=MibTableColumn
rohcRtpContextCCPs=_RohcRtpContextCCPs_Object((1,3,6,1,2,1,114,1,1,1,15),_RohcRtpContextCCPs_Type())
rohcRtpContextCCPs.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpContextCCPs.setStatus(_A)
_RohcRtpContextPktsLostPhysical_Type=Counter32
_RohcRtpContextPktsLostPhysical_Object=MibTableColumn
rohcRtpContextPktsLostPhysical=_RohcRtpContextPktsLostPhysical_Object((1,3,6,1,2,1,114,1,1,1,16),_RohcRtpContextPktsLostPhysical_Type())
rohcRtpContextPktsLostPhysical.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpContextPktsLostPhysical.setStatus(_A)
_RohcRtpContextPktsLostPreLink_Type=Counter32
_RohcRtpContextPktsLostPreLink_Object=MibTableColumn
rohcRtpContextPktsLostPreLink=_RohcRtpContextPktsLostPreLink_Object((1,3,6,1,2,1,114,1,1,1,17),_RohcRtpContextPktsLostPreLink_Type())
rohcRtpContextPktsLostPreLink.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpContextPktsLostPreLink.setStatus(_A)
_RohcRtpPacketSizeTable_Object=MibTable
rohcRtpPacketSizeTable=_RohcRtpPacketSizeTable_Object((1,3,6,1,2,1,114,1,2))
if mibBuilder.loadTexts:rohcRtpPacketSizeTable.setStatus(_A)
_RohcRtpPacketSizeEntry_Object=MibTableRow
rohcRtpPacketSizeEntry=_RohcRtpPacketSizeEntry_Object((1,3,6,1,2,1,114,1,2,1))
rohcRtpPacketSizeEntry.setIndexNames((0,_D,_G),(0,_D,_H),(0,_B,_J))
if mibBuilder.loadTexts:rohcRtpPacketSizeEntry.setStatus(_A)
class _RohcRtpPacketSize_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4294967295))
_RohcRtpPacketSize_Type.__name__=_E
_RohcRtpPacketSize_Object=MibTableColumn
rohcRtpPacketSize=_RohcRtpPacketSize_Object((1,3,6,1,2,1,114,1,2,1,3),_RohcRtpPacketSize_Type())
rohcRtpPacketSize.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rohcRtpPacketSize.setStatus(_A)
_RohcRtpPacketSizePreferred_Type=TruthValue
_RohcRtpPacketSizePreferred_Object=MibTableColumn
rohcRtpPacketSizePreferred=_RohcRtpPacketSizePreferred_Object((1,3,6,1,2,1,114,1,2,1,4),_RohcRtpPacketSizePreferred_Type())
rohcRtpPacketSizePreferred.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpPacketSizePreferred.setStatus(_A)
_RohcRtpPacketSizeUsed_Type=TruthValue
_RohcRtpPacketSizeUsed_Object=MibTableColumn
rohcRtpPacketSizeUsed=_RohcRtpPacketSizeUsed_Object((1,3,6,1,2,1,114,1,2,1,5),_RohcRtpPacketSizeUsed_Type())
rohcRtpPacketSizeUsed.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpPacketSizeUsed.setStatus(_A)
class _RohcRtpPacketSizeRestrictedType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('nhpOnly',1),('rhpOnly',2),('noRestrictions',3)))
_RohcRtpPacketSizeRestrictedType_Type.__name__=_F
_RohcRtpPacketSizeRestrictedType_Object=MibTableColumn
rohcRtpPacketSizeRestrictedType=_RohcRtpPacketSizeRestrictedType_Object((1,3,6,1,2,1,114,1,2,1,6),_RohcRtpPacketSizeRestrictedType_Type())
rohcRtpPacketSizeRestrictedType.setMaxAccess(_C)
if mibBuilder.loadTexts:rohcRtpPacketSizeRestrictedType.setStatus(_A)
_RohcRtpConformance_ObjectIdentity=ObjectIdentity
rohcRtpConformance=_RohcRtpConformance_ObjectIdentity((1,3,6,1,2,1,114,2))
_RohcRtpCompliances_ObjectIdentity=ObjectIdentity
rohcRtpCompliances=_RohcRtpCompliances_ObjectIdentity((1,3,6,1,2,1,114,2,1))
_RohcRtpGroups_ObjectIdentity=ObjectIdentity
rohcRtpGroups=_RohcRtpGroups_ObjectIdentity((1,3,6,1,2,1,114,2,2))
rohcRtpContextGroup=ObjectGroup((1,3,6,1,2,1,114,2,2,1))
rohcRtpContextGroup.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:rohcRtpContextGroup.setStatus(_A)
rohcRtpPacketSizesGroup=ObjectGroup((1,3,6,1,2,1,114,2,2,2))
rohcRtpPacketSizesGroup.setObjects(*((_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T)))
if mibBuilder.loadTexts:rohcRtpPacketSizesGroup.setStatus(_A)
rohcRtpStatisticsGroup=ObjectGroup((1,3,6,1,2,1,114,2,2,3))
rohcRtpStatisticsGroup.setObjects(*((_B,_U),(_B,_V),(_B,_W),(_B,_X),(_B,_Y),(_B,_Z),(_B,_a),(_B,_b)))
if mibBuilder.loadTexts:rohcRtpStatisticsGroup.setStatus(_A)
rohcRtpCompliance=ModuleCompliance((1,3,6,1,2,1,114,2,1,1))
rohcRtpCompliance.setObjects(*((_B,_c),(_B,_d),(_B,_e)))
if mibBuilder.loadTexts:rohcRtpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rohcRtpMIB':rohcRtpMIB,'rohcRtpObjects':rohcRtpObjects,'rohcRtpContextTable':rohcRtpContextTable,'rohcRtpContextEntry':rohcRtpContextEntry,_K:rohcRtpContextState,_L:rohcRtpContextMode,_M:rohcRtpContextAlwaysPad,_N:rohcRtpContextLargePktsAllowed,_O:rohcRtpContextVerifyPeriod,_P:rohcRtpContextSizesAllowed,_Q:rohcRtpContextSizesUsed,_U:rohcRtpContextACKs,_V:rohcRtpContextNACKs,_W:rohcRtpContextSNACKs,_X:rohcRtpContextNHPs,_Y:rohcRtpContextCSPs,_Z:rohcRtpContextCCPs,_a:rohcRtpContextPktsLostPhysical,_b:rohcRtpContextPktsLostPreLink,'rohcRtpPacketSizeTable':rohcRtpPacketSizeTable,'rohcRtpPacketSizeEntry':rohcRtpPacketSizeEntry,_J:rohcRtpPacketSize,_R:rohcRtpPacketSizePreferred,_S:rohcRtpPacketSizeUsed,_T:rohcRtpPacketSizeRestrictedType,'rohcRtpConformance':rohcRtpConformance,'rohcRtpCompliances':rohcRtpCompliances,'rohcRtpCompliance':rohcRtpCompliance,'rohcRtpGroups':rohcRtpGroups,_c:rohcRtpContextGroup,_d:rohcRtpPacketSizesGroup,_e:rohcRtpStatisticsGroup})