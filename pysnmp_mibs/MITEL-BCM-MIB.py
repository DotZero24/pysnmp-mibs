_N='mitelBCMChipGroup'
_M='mitelBCMPortGroup'
_L='mitelBCMChipType'
_K='mitelBCMChipRev'
_J='mitelBCMChipBIST'
_I='mitelBCMChipCount'
_H='mitelBCMPortRxLastSA'
_G='mitelBCMPortRxSAChanges'
_F='mitelBCMChipIndex'
_E='mitelBCMPortIndex'
_D='Integer32'
_C='read-only'
_B='MITEL-BCM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
mitelPropTransmission,=mibBuilder.importSymbols('MITEL-MIB','mitelPropTransmission')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
mitelBCM=ModuleIdentity((1,3,6,1,4,1,1027,4,2,1))
if mibBuilder.loadTexts:mitelBCM.setRevisions(('2009-03-17 00:00','2006-01-10 00:00','2005-10-04 01:00','2005-10-03 01:00','2005-09-30 01:00'))
_MitelBCMObjects_ObjectIdentity=ObjectIdentity
mitelBCMObjects=_MitelBCMObjects_ObjectIdentity((1,3,6,1,4,1,1027,4,2,1,1))
_MitelBCMPortTable_Object=MibTable
mitelBCMPortTable=_MitelBCMPortTable_Object((1,3,6,1,4,1,1027,4,2,1,1,1))
if mibBuilder.loadTexts:mitelBCMPortTable.setStatus(_A)
_MitelBCMPortTableEntry_Object=MibTableRow
mitelBCMPortTableEntry=_MitelBCMPortTableEntry_Object((1,3,6,1,4,1,1027,4,2,1,1,1,1))
mitelBCMPortTableEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:mitelBCMPortTableEntry.setStatus(_A)
_MitelBCMPortIndex_Type=InterfaceIndex
_MitelBCMPortIndex_Object=MibTableColumn
mitelBCMPortIndex=_MitelBCMPortIndex_Object((1,3,6,1,4,1,1027,4,2,1,1,1,1,1),_MitelBCMPortIndex_Type())
mitelBCMPortIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBCMPortIndex.setStatus(_A)
_MitelBCMPortRxSAChanges_Type=Counter32
_MitelBCMPortRxSAChanges_Object=MibTableColumn
mitelBCMPortRxSAChanges=_MitelBCMPortRxSAChanges_Object((1,3,6,1,4,1,1027,4,2,1,1,1,1,2),_MitelBCMPortRxSAChanges_Type())
mitelBCMPortRxSAChanges.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBCMPortRxSAChanges.setStatus(_A)
_MitelBCMPortRxLastSA_Type=PhysAddress
_MitelBCMPortRxLastSA_Object=MibTableColumn
mitelBCMPortRxLastSA=_MitelBCMPortRxLastSA_Object((1,3,6,1,4,1,1027,4,2,1,1,1,1,3),_MitelBCMPortRxLastSA_Type())
mitelBCMPortRxLastSA.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBCMPortRxLastSA.setStatus(_A)
_MitelBCMChipCount_Type=Integer32
_MitelBCMChipCount_Object=MibScalar
mitelBCMChipCount=_MitelBCMChipCount_Object((1,3,6,1,4,1,1027,4,2,1,1,2),_MitelBCMChipCount_Type())
mitelBCMChipCount.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBCMChipCount.setStatus(_A)
_MitelBCMChipTable_Object=MibTable
mitelBCMChipTable=_MitelBCMChipTable_Object((1,3,6,1,4,1,1027,4,2,1,1,3))
if mibBuilder.loadTexts:mitelBCMChipTable.setStatus(_A)
_MitelBCMChipTableEntry_Object=MibTableRow
mitelBCMChipTableEntry=_MitelBCMChipTableEntry_Object((1,3,6,1,4,1,1027,4,2,1,1,3,1))
mitelBCMChipTableEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:mitelBCMChipTableEntry.setStatus(_A)
class _MitelBCMChipIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_MitelBCMChipIndex_Type.__name__=_D
_MitelBCMChipIndex_Object=MibTableColumn
mitelBCMChipIndex=_MitelBCMChipIndex_Object((1,3,6,1,4,1,1027,4,2,1,1,3,1,1),_MitelBCMChipIndex_Type())
mitelBCMChipIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBCMChipIndex.setStatus(_A)
class _MitelBCMChipBIST_Type(Bits):namedValues=NamedValues(*(('bcRam',0),('ipDbm',1),('mRam',2),('gmRam',3)))
_MitelBCMChipBIST_Type.__name__='Bits'
_MitelBCMChipBIST_Object=MibTableColumn
mitelBCMChipBIST=_MitelBCMChipBIST_Object((1,3,6,1,4,1,1027,4,2,1,1,3,1,2),_MitelBCMChipBIST_Type())
mitelBCMChipBIST.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBCMChipBIST.setStatus(_A)
_MitelBCMChipRev_Type=DisplayString
_MitelBCMChipRev_Object=MibTableColumn
mitelBCMChipRev=_MitelBCMChipRev_Object((1,3,6,1,4,1,1027,4,2,1,1,3,1,3),_MitelBCMChipRev_Type())
mitelBCMChipRev.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBCMChipRev.setStatus(_A)
class _MitelBCMChipType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('bcm5380m',1),('bcm5325e',2),('bcm5324m',3),('bcmOther',4)))
_MitelBCMChipType_Type.__name__=_D
_MitelBCMChipType_Object=MibTableColumn
mitelBCMChipType=_MitelBCMChipType_Object((1,3,6,1,4,1,1027,4,2,1,1,3,1,4),_MitelBCMChipType_Type())
mitelBCMChipType.setMaxAccess(_C)
if mibBuilder.loadTexts:mitelBCMChipType.setStatus(_A)
_MitelBCMConformance_ObjectIdentity=ObjectIdentity
mitelBCMConformance=_MitelBCMConformance_ObjectIdentity((1,3,6,1,4,1,1027,4,2,1,2))
_MitelBCMCompliances_ObjectIdentity=ObjectIdentity
mitelBCMCompliances=_MitelBCMCompliances_ObjectIdentity((1,3,6,1,4,1,1027,4,2,1,2,1))
_MitelBCMGroups_ObjectIdentity=ObjectIdentity
mitelBCMGroups=_MitelBCMGroups_ObjectIdentity((1,3,6,1,4,1,1027,4,2,1,2,2))
mitelBCMPortGroup=ObjectGroup((1,3,6,1,4,1,1027,4,2,1,2,2,1))
mitelBCMPortGroup.setObjects(*((_B,_E),(_B,_G),(_B,_H)))
if mibBuilder.loadTexts:mitelBCMPortGroup.setStatus(_A)
mitelBCMChipGroup=ObjectGroup((1,3,6,1,4,1,1027,4,2,1,2,2,2))
mitelBCMChipGroup.setObjects(*((_B,_I),(_B,_F),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:mitelBCMChipGroup.setStatus(_A)
mitelBCMSwitchCompliance=ModuleCompliance((1,3,6,1,4,1,1027,4,2,1,2,1,1))
mitelBCMSwitchCompliance.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:mitelBCMSwitchCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'mitelBCM':mitelBCM,'mitelBCMObjects':mitelBCMObjects,'mitelBCMPortTable':mitelBCMPortTable,'mitelBCMPortTableEntry':mitelBCMPortTableEntry,_E:mitelBCMPortIndex,_G:mitelBCMPortRxSAChanges,_H:mitelBCMPortRxLastSA,_I:mitelBCMChipCount,'mitelBCMChipTable':mitelBCMChipTable,'mitelBCMChipTableEntry':mitelBCMChipTableEntry,_F:mitelBCMChipIndex,_J:mitelBCMChipBIST,_K:mitelBCMChipRev,_L:mitelBCMChipType,'mitelBCMConformance':mitelBCMConformance,'mitelBCMCompliances':mitelBCMCompliances,'mitelBCMSwitchCompliance':mitelBCMSwitchCompliance,'mitelBCMGroups':mitelBCMGroups,_M:mitelBCMPortGroup,_N:mitelBCMChipGroup})