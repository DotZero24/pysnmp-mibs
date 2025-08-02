_L='rohcUncmprStatisticsGroup'
_K='rohcUncmprContextGroup'
_J='rohcUncmprContextACKs'
_I='rohcUncmprContextMode'
_H='rohcUncmprContextState'
_G='rohcContextCID'
_F='rohcChannelID'
_E='read-only'
_D='Integer32'
_C='ROHC-MIB'
_B='ROHC-UNCOMPRESSED-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
rohcChannelID,rohcContextCID=mibBuilder.importSymbols(_C,_F,_G)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso,mib_2=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso','mib-2')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
rohcUncmprMIB=ModuleIdentity((1,3,6,1,2,1,113))
if mibBuilder.loadTexts:rohcUncmprMIB.setRevisions(('2004-06-03 00:00',))
_RohcUncmprObjects_ObjectIdentity=ObjectIdentity
rohcUncmprObjects=_RohcUncmprObjects_ObjectIdentity((1,3,6,1,2,1,113,1))
_RohcUncmprContextTable_Object=MibTable
rohcUncmprContextTable=_RohcUncmprContextTable_Object((1,3,6,1,2,1,113,1,1))
if mibBuilder.loadTexts:rohcUncmprContextTable.setStatus(_A)
_RohcUncmprContextEntry_Object=MibTableRow
rohcUncmprContextEntry=_RohcUncmprContextEntry_Object((1,3,6,1,2,1,113,1,1,1))
rohcUncmprContextEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:rohcUncmprContextEntry.setStatus(_A)
class _RohcUncmprContextState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('initAndRefresh',1),('normal',2),('noContext',3),('fullContext',4)))
_RohcUncmprContextState_Type.__name__=_D
_RohcUncmprContextState_Object=MibTableColumn
rohcUncmprContextState=_RohcUncmprContextState_Object((1,3,6,1,2,1,113,1,1,1,3),_RohcUncmprContextState_Type())
rohcUncmprContextState.setMaxAccess(_E)
if mibBuilder.loadTexts:rohcUncmprContextState.setStatus(_A)
class _RohcUncmprContextMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('unidirectional',1),('bidirectional',2)))
_RohcUncmprContextMode_Type.__name__=_D
_RohcUncmprContextMode_Object=MibTableColumn
rohcUncmprContextMode=_RohcUncmprContextMode_Object((1,3,6,1,2,1,113,1,1,1,4),_RohcUncmprContextMode_Type())
rohcUncmprContextMode.setMaxAccess(_E)
if mibBuilder.loadTexts:rohcUncmprContextMode.setStatus(_A)
_RohcUncmprContextACKs_Type=Counter32
_RohcUncmprContextACKs_Object=MibTableColumn
rohcUncmprContextACKs=_RohcUncmprContextACKs_Object((1,3,6,1,2,1,113,1,1,1,5),_RohcUncmprContextACKs_Type())
rohcUncmprContextACKs.setMaxAccess(_E)
if mibBuilder.loadTexts:rohcUncmprContextACKs.setStatus(_A)
_RohcUncmprConformance_ObjectIdentity=ObjectIdentity
rohcUncmprConformance=_RohcUncmprConformance_ObjectIdentity((1,3,6,1,2,1,113,2))
_RohcUncmprCompliances_ObjectIdentity=ObjectIdentity
rohcUncmprCompliances=_RohcUncmprCompliances_ObjectIdentity((1,3,6,1,2,1,113,2,1))
_RohcUncmprGroups_ObjectIdentity=ObjectIdentity
rohcUncmprGroups=_RohcUncmprGroups_ObjectIdentity((1,3,6,1,2,1,113,2,2))
rohcUncmprContextGroup=ObjectGroup((1,3,6,1,2,1,113,2,2,1))
rohcUncmprContextGroup.setObjects(*((_B,_H),(_B,_I)))
if mibBuilder.loadTexts:rohcUncmprContextGroup.setStatus(_A)
rohcUncmprStatisticsGroup=ObjectGroup((1,3,6,1,2,1,113,2,2,2))
rohcUncmprStatisticsGroup.setObjects((_B,_J))
if mibBuilder.loadTexts:rohcUncmprStatisticsGroup.setStatus(_A)
rohcUncmprCompliance=ModuleCompliance((1,3,6,1,2,1,113,2,1,1))
rohcUncmprCompliance.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:rohcUncmprCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'rohcUncmprMIB':rohcUncmprMIB,'rohcUncmprObjects':rohcUncmprObjects,'rohcUncmprContextTable':rohcUncmprContextTable,'rohcUncmprContextEntry':rohcUncmprContextEntry,_H:rohcUncmprContextState,_I:rohcUncmprContextMode,_J:rohcUncmprContextACKs,'rohcUncmprConformance':rohcUncmprConformance,'rohcUncmprCompliances':rohcUncmprCompliances,'rohcUncmprCompliance':rohcUncmprCompliance,'rohcUncmprGroups':rohcUncmprGroups,_K:rohcUncmprContextGroup,_L:rohcUncmprStatisticsGroup})