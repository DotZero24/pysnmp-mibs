_c='gmplsOutSegmentExtraParamsPtr'
_b='gmplsOutSegmentTTLDecrement'
_a='gmplsOutSegmentDirection'
_Z='gmplsInSegmentExtraParamsPtr'
_Y='gmplsInSegmentDirection'
_X='gmplsInterfaceRsvpHelloPeriod'
_W='gmplsInterfaceSignalingCaps'
_V='mplsOutSegmentIndex'
_U='mplsLsrNotificationGroup'
_T='mplsInterfaceIndex'
_S='mplsInSegmentIndex'
_R='gmplsOutSegmentGroup'
_Q='gmplsInSegmentGroup'
_P='gmplsInterfaceGroup'
_O='RowPointer'
_N='Unsigned32'
_M='mplsXCGroup'
_L='mplsPerfGroup'
_K='mplsOutSegmentGroup'
_J='mplsInterfaceGroup'
_I='mplsInSegmentGroup'
_H='ifGeneralInformationGroup'
_G='ifCounterDiscontinuityGroup'
_F='GmplsSegmentDirectionTC'
_E='IF-MIB'
_D='read-create'
_C='GMPLS-LSR-STD-MIB'
_B='MPLS-LSR-STD-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
GmplsSegmentDirectionTC,=mibBuilder.importSymbols('GMPLS-TC-STD-MIB',_F)
ifCounterDiscontinuityGroup,ifGeneralInformationGroup=mibBuilder.importSymbols(_E,_G,_H)
mplsInSegmentGroup,mplsInSegmentIndex,mplsInterfaceGroup,mplsInterfaceIndex,mplsLsrNotificationGroup,mplsOutSegmentGroup,mplsOutSegmentIndex,mplsPerfGroup,mplsXCGroup=mibBuilder.importSymbols(_B,_I,_S,_J,_T,_U,_K,_V,_L,_M)
mplsStdMIB,=mibBuilder.importSymbols('MPLS-TC-STD-MIB','mplsStdMIB')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,zeroDotZero=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_N,'iso','zeroDotZero')
DisplayString,PhysAddress,RowPointer,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress',_O,'TextualConvention')
gmplsLsrStdMIB=ModuleIdentity((1,3,6,1,2,1,10,166,15))
if mibBuilder.loadTexts:gmplsLsrStdMIB.setRevisions(('2007-02-27 00:00',))
_GmplsLsrObjects_ObjectIdentity=ObjectIdentity
gmplsLsrObjects=_GmplsLsrObjects_ObjectIdentity((1,3,6,1,2,1,10,166,15,1))
_GmplsInterfaceTable_Object=MibTable
gmplsInterfaceTable=_GmplsInterfaceTable_Object((1,3,6,1,2,1,10,166,15,1,1))
if mibBuilder.loadTexts:gmplsInterfaceTable.setStatus(_A)
_GmplsInterfaceEntry_Object=MibTableRow
gmplsInterfaceEntry=_GmplsInterfaceEntry_Object((1,3,6,1,2,1,10,166,15,1,1,1))
gmplsInterfaceEntry.setIndexNames((0,_B,_T))
if mibBuilder.loadTexts:gmplsInterfaceEntry.setStatus(_A)
class _GmplsInterfaceSignalingCaps_Type(Bits):defaultBinValue='01';namedValues=NamedValues(*(('unknown',0),('rsvpGmpls',1),('crldpGmpls',2),('otherGmpls',3)))
_GmplsInterfaceSignalingCaps_Type.__name__='Bits'
_GmplsInterfaceSignalingCaps_Object=MibTableColumn
gmplsInterfaceSignalingCaps=_GmplsInterfaceSignalingCaps_Object((1,3,6,1,2,1,10,166,15,1,1,1,1),_GmplsInterfaceSignalingCaps_Type())
gmplsInterfaceSignalingCaps.setMaxAccess(_D)
if mibBuilder.loadTexts:gmplsInterfaceSignalingCaps.setStatus(_A)
class _GmplsInterfaceRsvpHelloPeriod_Type(Unsigned32):defaultValue=3000
_GmplsInterfaceRsvpHelloPeriod_Type.__name__=_N
_GmplsInterfaceRsvpHelloPeriod_Object=MibTableColumn
gmplsInterfaceRsvpHelloPeriod=_GmplsInterfaceRsvpHelloPeriod_Object((1,3,6,1,2,1,10,166,15,1,1,1,2),_GmplsInterfaceRsvpHelloPeriod_Type())
gmplsInterfaceRsvpHelloPeriod.setMaxAccess(_D)
if mibBuilder.loadTexts:gmplsInterfaceRsvpHelloPeriod.setStatus(_A)
if mibBuilder.loadTexts:gmplsInterfaceRsvpHelloPeriod.setUnits('milliseconds')
_GmplsInSegmentTable_Object=MibTable
gmplsInSegmentTable=_GmplsInSegmentTable_Object((1,3,6,1,2,1,10,166,15,1,2))
if mibBuilder.loadTexts:gmplsInSegmentTable.setStatus(_A)
_GmplsInSegmentEntry_Object=MibTableRow
gmplsInSegmentEntry=_GmplsInSegmentEntry_Object((1,3,6,1,2,1,10,166,15,1,2,1))
gmplsInSegmentEntry.setIndexNames((0,_B,_S))
if mibBuilder.loadTexts:gmplsInSegmentEntry.setStatus(_A)
class _GmplsInSegmentDirection_Type(GmplsSegmentDirectionTC):defaultValue=1
_GmplsInSegmentDirection_Type.__name__=_F
_GmplsInSegmentDirection_Object=MibTableColumn
gmplsInSegmentDirection=_GmplsInSegmentDirection_Object((1,3,6,1,2,1,10,166,15,1,2,1,1),_GmplsInSegmentDirection_Type())
gmplsInSegmentDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:gmplsInSegmentDirection.setStatus(_A)
class _GmplsInSegmentExtraParamsPtr_Type(RowPointer):defaultValue=0,0
_GmplsInSegmentExtraParamsPtr_Type.__name__=_O
_GmplsInSegmentExtraParamsPtr_Object=MibTableColumn
gmplsInSegmentExtraParamsPtr=_GmplsInSegmentExtraParamsPtr_Object((1,3,6,1,2,1,10,166,15,1,2,1,2),_GmplsInSegmentExtraParamsPtr_Type())
gmplsInSegmentExtraParamsPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:gmplsInSegmentExtraParamsPtr.setStatus(_A)
_GmplsOutSegmentTable_Object=MibTable
gmplsOutSegmentTable=_GmplsOutSegmentTable_Object((1,3,6,1,2,1,10,166,15,1,3))
if mibBuilder.loadTexts:gmplsOutSegmentTable.setStatus(_A)
_GmplsOutSegmentEntry_Object=MibTableRow
gmplsOutSegmentEntry=_GmplsOutSegmentEntry_Object((1,3,6,1,2,1,10,166,15,1,3,1))
gmplsOutSegmentEntry.setIndexNames((0,_B,_V))
if mibBuilder.loadTexts:gmplsOutSegmentEntry.setStatus(_A)
class _GmplsOutSegmentDirection_Type(GmplsSegmentDirectionTC):defaultValue=1
_GmplsOutSegmentDirection_Type.__name__=_F
_GmplsOutSegmentDirection_Object=MibTableColumn
gmplsOutSegmentDirection=_GmplsOutSegmentDirection_Object((1,3,6,1,2,1,10,166,15,1,3,1,1),_GmplsOutSegmentDirection_Type())
gmplsOutSegmentDirection.setMaxAccess(_D)
if mibBuilder.loadTexts:gmplsOutSegmentDirection.setStatus(_A)
class _GmplsOutSegmentTTLDecrement_Type(Unsigned32):defaultValue=0
_GmplsOutSegmentTTLDecrement_Type.__name__=_N
_GmplsOutSegmentTTLDecrement_Object=MibTableColumn
gmplsOutSegmentTTLDecrement=_GmplsOutSegmentTTLDecrement_Object((1,3,6,1,2,1,10,166,15,1,3,1,2),_GmplsOutSegmentTTLDecrement_Type())
gmplsOutSegmentTTLDecrement.setMaxAccess(_D)
if mibBuilder.loadTexts:gmplsOutSegmentTTLDecrement.setStatus(_A)
class _GmplsOutSegmentExtraParamsPtr_Type(RowPointer):defaultValue=0,0
_GmplsOutSegmentExtraParamsPtr_Type.__name__=_O
_GmplsOutSegmentExtraParamsPtr_Object=MibTableColumn
gmplsOutSegmentExtraParamsPtr=_GmplsOutSegmentExtraParamsPtr_Object((1,3,6,1,2,1,10,166,15,1,3,1,3),_GmplsOutSegmentExtraParamsPtr_Type())
gmplsOutSegmentExtraParamsPtr.setMaxAccess(_D)
if mibBuilder.loadTexts:gmplsOutSegmentExtraParamsPtr.setStatus(_A)
_GmplsLsrConformance_ObjectIdentity=ObjectIdentity
gmplsLsrConformance=_GmplsLsrConformance_ObjectIdentity((1,3,6,1,2,1,10,166,15,2))
_GmplsLsrGroups_ObjectIdentity=ObjectIdentity
gmplsLsrGroups=_GmplsLsrGroups_ObjectIdentity((1,3,6,1,2,1,10,166,15,2,1))
_GmplsLsrCompliances_ObjectIdentity=ObjectIdentity
gmplsLsrCompliances=_GmplsLsrCompliances_ObjectIdentity((1,3,6,1,2,1,10,166,15,2,2))
gmplsInterfaceGroup=ObjectGroup((1,3,6,1,2,1,10,166,15,2,1,1))
gmplsInterfaceGroup.setObjects(*((_C,_W),(_C,_X)))
if mibBuilder.loadTexts:gmplsInterfaceGroup.setStatus(_A)
gmplsInSegmentGroup=ObjectGroup((1,3,6,1,2,1,10,166,15,2,1,2))
gmplsInSegmentGroup.setObjects(*((_C,_Y),(_C,_Z)))
if mibBuilder.loadTexts:gmplsInSegmentGroup.setStatus(_A)
gmplsOutSegmentGroup=ObjectGroup((1,3,6,1,2,1,10,166,15,2,1,3))
gmplsOutSegmentGroup.setObjects(*((_C,_a),(_C,_b),(_C,_c)))
if mibBuilder.loadTexts:gmplsOutSegmentGroup.setStatus(_A)
gmplsLsrModuleFullCompliance=ModuleCompliance((1,3,6,1,2,1,10,166,15,2,2,1))
gmplsLsrModuleFullCompliance.setObjects(*((_E,_H),(_E,_G),(_B,_J),(_B,_I),(_B,_K),(_B,_M),(_B,_L),(_B,_U),(_C,_P),(_C,_Q),(_C,_R)))
if mibBuilder.loadTexts:gmplsLsrModuleFullCompliance.setStatus(_A)
gmplsLsrModuleReadOnlyCompliance=ModuleCompliance((1,3,6,1,2,1,10,166,15,2,2,2))
gmplsLsrModuleReadOnlyCompliance.setObjects(*((_E,_H),(_E,_G),(_B,_J),(_B,_I),(_B,_K),(_B,_M),(_B,_L),(_C,_P),(_C,_Q),(_C,_R)))
if mibBuilder.loadTexts:gmplsLsrModuleReadOnlyCompliance.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'gmplsLsrStdMIB':gmplsLsrStdMIB,'gmplsLsrObjects':gmplsLsrObjects,'gmplsInterfaceTable':gmplsInterfaceTable,'gmplsInterfaceEntry':gmplsInterfaceEntry,_W:gmplsInterfaceSignalingCaps,_X:gmplsInterfaceRsvpHelloPeriod,'gmplsInSegmentTable':gmplsInSegmentTable,'gmplsInSegmentEntry':gmplsInSegmentEntry,_Y:gmplsInSegmentDirection,_Z:gmplsInSegmentExtraParamsPtr,'gmplsOutSegmentTable':gmplsOutSegmentTable,'gmplsOutSegmentEntry':gmplsOutSegmentEntry,_a:gmplsOutSegmentDirection,_b:gmplsOutSegmentTTLDecrement,_c:gmplsOutSegmentExtraParamsPtr,'gmplsLsrConformance':gmplsLsrConformance,'gmplsLsrGroups':gmplsLsrGroups,_P:gmplsInterfaceGroup,_Q:gmplsInSegmentGroup,_R:gmplsOutSegmentGroup,'gmplsLsrCompliances':gmplsLsrCompliances,'gmplsLsrModuleFullCompliance':gmplsLsrModuleFullCompliance,'gmplsLsrModuleReadOnlyCompliance':gmplsLsrModuleReadOnlyCompliance})