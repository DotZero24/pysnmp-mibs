_K='fbmGroup'
_J='fbmUsbDownstreamNbr'
_I='fbmUsbUpstreamNbr'
_H='fbmProvEqptType'
_G='fbmMoId'
_F='read-only'
_E='read-write'
_D='entPhysicalIndex'
_C='ENTITY-MIB'
_B='INFINERA-ENTITY-FBM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
entPhysicalIndex,=mibBuilder.importSymbols(_C,_D)
equipment,=mibBuilder.importSymbols('INFINERA-REG-MIB','equipment')
InfnEqptType,=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnEqptType')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
fbmMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,1,55))
_FbmTable_Object=MibTable
fbmTable=_FbmTable_Object((1,3,6,1,4,1,21296,2,2,2,1,55,1))
if mibBuilder.loadTexts:fbmTable.setStatus(_A)
_FbmEntry_Object=MibTableRow
fbmEntry=_FbmEntry_Object((1,3,6,1,4,1,21296,2,2,2,1,55,1,1))
fbmEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:fbmEntry.setStatus(_A)
_FbmMoId_Type=DisplayString
_FbmMoId_Object=MibTableColumn
fbmMoId=_FbmMoId_Object((1,3,6,1,4,1,21296,2,2,2,1,55,1,1,1),_FbmMoId_Type())
fbmMoId.setMaxAccess(_E)
if mibBuilder.loadTexts:fbmMoId.setStatus(_A)
_FbmProvEqptType_Type=InfnEqptType
_FbmProvEqptType_Object=MibTableColumn
fbmProvEqptType=_FbmProvEqptType_Object((1,3,6,1,4,1,21296,2,2,2,1,55,1,1,2),_FbmProvEqptType_Type())
fbmProvEqptType.setMaxAccess(_E)
if mibBuilder.loadTexts:fbmProvEqptType.setStatus(_A)
_FbmUsbUpstreamNbr_Type=DisplayString
_FbmUsbUpstreamNbr_Object=MibTableColumn
fbmUsbUpstreamNbr=_FbmUsbUpstreamNbr_Object((1,3,6,1,4,1,21296,2,2,2,1,55,1,1,3),_FbmUsbUpstreamNbr_Type())
fbmUsbUpstreamNbr.setMaxAccess(_F)
if mibBuilder.loadTexts:fbmUsbUpstreamNbr.setStatus(_A)
_FbmUsbDownstreamNbr_Type=DisplayString
_FbmUsbDownstreamNbr_Object=MibTableColumn
fbmUsbDownstreamNbr=_FbmUsbDownstreamNbr_Object((1,3,6,1,4,1,21296,2,2,2,1,55,1,1,4),_FbmUsbDownstreamNbr_Type())
fbmUsbDownstreamNbr.setMaxAccess(_F)
if mibBuilder.loadTexts:fbmUsbDownstreamNbr.setStatus(_A)
_FbmConformance_ObjectIdentity=ObjectIdentity
fbmConformance=_FbmConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,55,3))
_FbmCompliances_ObjectIdentity=ObjectIdentity
fbmCompliances=_FbmCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,55,3,1))
_FbmGroups_ObjectIdentity=ObjectIdentity
fbmGroups=_FbmGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,1,55,3,2))
fbmGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,1,55,3,2,1))
fbmGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J)))
if mibBuilder.loadTexts:fbmGroup.setStatus(_A)
fbmCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,1,55,3,1,1))
fbmCompliance.setObjects((_B,_K))
if mibBuilder.loadTexts:fbmCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fbmMIB':fbmMIB,'fbmTable':fbmTable,'fbmEntry':fbmEntry,_G:fbmMoId,_H:fbmProvEqptType,_I:fbmUsbUpstreamNbr,_J:fbmUsbDownstreamNbr,'fbmConformance':fbmConformance,'fbmCompliances':fbmCompliances,'fbmCompliance':fbmCompliance,'fbmGroups':fbmGroups,_K:fbmGroup})