_N='ibmBnaDirLuName'
_M='ibmBnaNnTgFRNum'
_L='ibmBnaNnTgFRDest'
_K='ibmBnaNnTgFROwner'
_J='ibmBnaNnTgFRFrsn'
_I='ibmBnaNnNodeFRName'
_H='ibmBnaNnNodeFRFrsn'
_G='ibmBnaLocalTgNum'
_F='ibmBnaLocalTgDest'
_E='Integer32'
_D='DisplayString'
_C='IBMBNA-MIB'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'PhysAddress','TextualConvention')
class TruthValue(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('true',1),('false',2)))
_Ibm_ObjectIdentity=ObjectIdentity
ibm=_Ibm_ObjectIdentity((1,3,6,1,4,1,2))
_IbmArchitecture_ObjectIdentity=ObjectIdentity
ibmArchitecture=_IbmArchitecture_ObjectIdentity((1,3,6,1,4,1,2,5))
_IbmBna_ObjectIdentity=ObjectIdentity
ibmBna=_IbmBna_ObjectIdentity((1,3,6,1,4,1,2,5,21))
_IbmBnaObjects_ObjectIdentity=ObjectIdentity
ibmBnaObjects=_IbmBnaObjects_ObjectIdentity((1,3,6,1,4,1,2,5,21,1))
_IbmBnaLocalTgTable_Object=MibTable
ibmBnaLocalTgTable=_IbmBnaLocalTgTable_Object((1,3,6,1,4,1,2,5,21,1,1))
if mibBuilder.loadTexts:ibmBnaLocalTgTable.setStatus(_A)
_IbmBnaLocalTgEntry_Object=MibTableRow
ibmBnaLocalTgEntry=_IbmBnaLocalTgEntry_Object((1,3,6,1,4,1,2,5,21,1,1,1))
ibmBnaLocalTgEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:ibmBnaLocalTgEntry.setStatus(_A)
class _IbmBnaLocalTgDest_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmBnaLocalTgDest_Type.__name__=_D
_IbmBnaLocalTgDest_Object=MibTableColumn
ibmBnaLocalTgDest=_IbmBnaLocalTgDest_Object((1,3,6,1,4,1,2,5,21,1,1,1,1),_IbmBnaLocalTgDest_Type())
ibmBnaLocalTgDest.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmBnaLocalTgDest.setStatus(_A)
class _IbmBnaLocalTgNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmBnaLocalTgNum_Type.__name__=_E
_IbmBnaLocalTgNum_Object=MibTableColumn
ibmBnaLocalTgNum=_IbmBnaLocalTgNum_Object((1,3,6,1,4,1,2,5,21,1,1,1,2),_IbmBnaLocalTgNum_Type())
ibmBnaLocalTgNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmBnaLocalTgNum.setStatus(_A)
class _IbmBnaLocalTgLinkType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*(('other',1),('uplink',2),('downlink',3),('downlinkToBranchNetworkNode',4),('unknown',255)))
_IbmBnaLocalTgLinkType_Type.__name__=_E
_IbmBnaLocalTgLinkType_Object=MibTableColumn
ibmBnaLocalTgLinkType=_IbmBnaLocalTgLinkType_Object((1,3,6,1,4,1,2,5,21,1,1,1,3),_IbmBnaLocalTgLinkType_Type())
ibmBnaLocalTgLinkType.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmBnaLocalTgLinkType.setStatus(_A)
_IbmBnaNnTopologyFRTable_Object=MibTable
ibmBnaNnTopologyFRTable=_IbmBnaNnTopologyFRTable_Object((1,3,6,1,4,1,2,5,21,1,2))
if mibBuilder.loadTexts:ibmBnaNnTopologyFRTable.setStatus(_A)
_IbmBnaNnTopologyFREntry_Object=MibTableRow
ibmBnaNnTopologyFREntry=_IbmBnaNnTopologyFREntry_Object((1,3,6,1,4,1,2,5,21,1,2,1))
ibmBnaNnTopologyFREntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:ibmBnaNnTopologyFREntry.setStatus(_A)
_IbmBnaNnNodeFRFrsn_Type=Gauge32
_IbmBnaNnNodeFRFrsn_Object=MibTableColumn
ibmBnaNnNodeFRFrsn=_IbmBnaNnNodeFRFrsn_Object((1,3,6,1,4,1,2,5,21,1,2,1,1),_IbmBnaNnNodeFRFrsn_Type())
ibmBnaNnNodeFRFrsn.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmBnaNnNodeFRFrsn.setStatus(_A)
class _IbmBnaNnNodeFRName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmBnaNnNodeFRName_Type.__name__=_D
_IbmBnaNnNodeFRName_Object=MibTableColumn
ibmBnaNnNodeFRName=_IbmBnaNnNodeFRName_Object((1,3,6,1,4,1,2,5,21,1,2,1,2),_IbmBnaNnNodeFRName_Type())
ibmBnaNnNodeFRName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmBnaNnNodeFRName.setStatus(_A)
_IbmBnaNnNodeFRBranchAwareness_Type=TruthValue
_IbmBnaNnNodeFRBranchAwareness_Object=MibTableColumn
ibmBnaNnNodeFRBranchAwareness=_IbmBnaNnNodeFRBranchAwareness_Object((1,3,6,1,4,1,2,5,21,1,2,1,3),_IbmBnaNnNodeFRBranchAwareness_Type())
ibmBnaNnNodeFRBranchAwareness.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmBnaNnNodeFRBranchAwareness.setStatus(_A)
_IbmBnaNnTgTopologyFRTable_Object=MibTable
ibmBnaNnTgTopologyFRTable=_IbmBnaNnTgTopologyFRTable_Object((1,3,6,1,4,1,2,5,21,1,3))
if mibBuilder.loadTexts:ibmBnaNnTgTopologyFRTable.setStatus(_A)
_IbmBnaNnTgTopologyFREntry_Object=MibTableRow
ibmBnaNnTgTopologyFREntry=_IbmBnaNnTgTopologyFREntry_Object((1,3,6,1,4,1,2,5,21,1,3,1))
ibmBnaNnTgTopologyFREntry.setIndexNames((0,_C,_J),(0,_C,_K),(0,_C,_L),(0,_C,_M))
if mibBuilder.loadTexts:ibmBnaNnTgTopologyFREntry.setStatus(_A)
_IbmBnaNnTgFRFrsn_Type=Gauge32
_IbmBnaNnTgFRFrsn_Object=MibTableColumn
ibmBnaNnTgFRFrsn=_IbmBnaNnTgFRFrsn_Object((1,3,6,1,4,1,2,5,21,1,3,1,1),_IbmBnaNnTgFRFrsn_Type())
ibmBnaNnTgFRFrsn.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmBnaNnTgFRFrsn.setStatus(_A)
class _IbmBnaNnTgFROwner_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmBnaNnTgFROwner_Type.__name__=_D
_IbmBnaNnTgFROwner_Object=MibTableColumn
ibmBnaNnTgFROwner=_IbmBnaNnTgFROwner_Object((1,3,6,1,4,1,2,5,21,1,3,1,2),_IbmBnaNnTgFROwner_Type())
ibmBnaNnTgFROwner.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmBnaNnTgFROwner.setStatus(_A)
class _IbmBnaNnTgFRDest_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(3,17))
_IbmBnaNnTgFRDest_Type.__name__=_D
_IbmBnaNnTgFRDest_Object=MibTableColumn
ibmBnaNnTgFRDest=_IbmBnaNnTgFRDest_Object((1,3,6,1,4,1,2,5,21,1,3,1,3),_IbmBnaNnTgFRDest_Type())
ibmBnaNnTgFRDest.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmBnaNnTgFRDest.setStatus(_A)
class _IbmBnaNnTgFRNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmBnaNnTgFRNum_Type.__name__=_E
_IbmBnaNnTgFRNum_Object=MibTableColumn
ibmBnaNnTgFRNum=_IbmBnaNnTgFRNum_Object((1,3,6,1,4,1,2,5,21,1,3,1,4),_IbmBnaNnTgFRNum_Type())
ibmBnaNnTgFRNum.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmBnaNnTgFRNum.setStatus(_A)
_IbmBnaNnTgFRBranchTg_Type=TruthValue
_IbmBnaNnTgFRBranchTg_Object=MibTableColumn
ibmBnaNnTgFRBranchTg=_IbmBnaNnTgFRBranchTg_Object((1,3,6,1,4,1,2,5,21,1,3,1,5),_IbmBnaNnTgFRBranchTg_Type())
ibmBnaNnTgFRBranchTg.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmBnaNnTgFRBranchTg.setStatus(_A)
_IbmBnaDirTable_Object=MibTable
ibmBnaDirTable=_IbmBnaDirTable_Object((1,3,6,1,4,1,2,5,21,1,4))
if mibBuilder.loadTexts:ibmBnaDirTable.setStatus(_A)
_IbmBnaDirEntry_Object=MibTableRow
ibmBnaDirEntry=_IbmBnaDirEntry_Object((1,3,6,1,4,1,2,5,21,1,4,1))
ibmBnaDirEntry.setIndexNames((0,_C,_N))
if mibBuilder.loadTexts:ibmBnaDirEntry.setStatus(_A)
class _IbmBnaDirLuName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,17))
_IbmBnaDirLuName_Type.__name__=_D
_IbmBnaDirLuName_Object=MibTableColumn
ibmBnaDirLuName=_IbmBnaDirLuName_Object((1,3,6,1,4,1,2,5,21,1,4,1,1),_IbmBnaDirLuName_Type())
ibmBnaDirLuName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmBnaDirLuName.setStatus(_A)
class _IbmBnaDirApparentLuOwnerName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,0),ValueSizeConstraint(3,17))
_IbmBnaDirApparentLuOwnerName_Type.__name__=_D
_IbmBnaDirApparentLuOwnerName_Object=MibTableColumn
ibmBnaDirApparentLuOwnerName=_IbmBnaDirApparentLuOwnerName_Object((1,3,6,1,4,1,2,5,21,1,4,1,2),_IbmBnaDirApparentLuOwnerName_Type())
ibmBnaDirApparentLuOwnerName.setMaxAccess(_B)
if mibBuilder.loadTexts:ibmBnaDirApparentLuOwnerName.setStatus(_A)
_IbmBnaConformance_ObjectIdentity=ObjectIdentity
ibmBnaConformance=_IbmBnaConformance_ObjectIdentity((1,3,6,1,4,1,2,5,21,2))
_IbmBnaCompliances_ObjectIdentity=ObjectIdentity
ibmBnaCompliances=_IbmBnaCompliances_ObjectIdentity((1,3,6,1,4,1,2,5,21,2,1))
_IbmBnaConfGroups_ObjectIdentity=ObjectIdentity
ibmBnaConfGroups=_IbmBnaConfGroups_ObjectIdentity((1,3,6,1,4,1,2,5,21,2,2))
mibBuilder.exportSymbols(_C,**{'TruthValue':TruthValue,'ibm':ibm,'ibmArchitecture':ibmArchitecture,'ibmBna':ibmBna,'ibmBnaObjects':ibmBnaObjects,'ibmBnaLocalTgTable':ibmBnaLocalTgTable,'ibmBnaLocalTgEntry':ibmBnaLocalTgEntry,_F:ibmBnaLocalTgDest,_G:ibmBnaLocalTgNum,'ibmBnaLocalTgLinkType':ibmBnaLocalTgLinkType,'ibmBnaNnTopologyFRTable':ibmBnaNnTopologyFRTable,'ibmBnaNnTopologyFREntry':ibmBnaNnTopologyFREntry,_H:ibmBnaNnNodeFRFrsn,_I:ibmBnaNnNodeFRName,'ibmBnaNnNodeFRBranchAwareness':ibmBnaNnNodeFRBranchAwareness,'ibmBnaNnTgTopologyFRTable':ibmBnaNnTgTopologyFRTable,'ibmBnaNnTgTopologyFREntry':ibmBnaNnTgTopologyFREntry,_J:ibmBnaNnTgFRFrsn,_K:ibmBnaNnTgFROwner,_L:ibmBnaNnTgFRDest,_M:ibmBnaNnTgFRNum,'ibmBnaNnTgFRBranchTg':ibmBnaNnTgFRBranchTg,'ibmBnaDirTable':ibmBnaDirTable,'ibmBnaDirEntry':ibmBnaDirEntry,_N:ibmBnaDirLuName,'ibmBnaDirApparentLuOwnerName':ibmBnaDirApparentLuOwnerName,'ibmBnaConformance':ibmBnaConformance,'ibmBnaCompliances':ibmBnaCompliances,'ibmBnaConfGroups':ibmBnaConfGroups})