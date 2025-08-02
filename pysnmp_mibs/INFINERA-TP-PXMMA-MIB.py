_O='pxmMaGroup'
_N='pxmMaMDLevel'
_M='pxmMaMDName'
_L='pxmMaSenderIDTLV'
_K='pxmMaMANameFormat'
_J='pxmMaCcmInterval'
_I='pxmMaMDAid'
_H='pxmMaRMepAgeOutInterval'
_G='pxmMaMAName'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='read-write'
_B='INFINERA-TP-PXMMA-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
InfnCcmInterval,InfnMANameFormat,InfnSenderIDTLV=mibBuilder.importSymbols('INFINERA-TC-MIB','InfnCcmInterval','InfnMANameFormat','InfnSenderIDTLV')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
pxmMaMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,79))
if mibBuilder.loadTexts:pxmMaMIB.setRevisions(('2016-05-30 00:00',))
_PxmMaTable_Object=MibTable
pxmMaTable=_PxmMaTable_Object((1,3,6,1,4,1,21296,2,2,2,2,79,1))
if mibBuilder.loadTexts:pxmMaTable.setStatus(_A)
_PxmMaEntry_Object=MibTableRow
pxmMaEntry=_PxmMaEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,79,1,1))
pxmMaEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:pxmMaEntry.setStatus(_A)
_PxmMaMAName_Type=DisplayString
_PxmMaMAName_Object=MibTableColumn
pxmMaMAName=_PxmMaMAName_Object((1,3,6,1,4,1,21296,2,2,2,2,79,1,1,1),_PxmMaMAName_Type())
pxmMaMAName.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmMaMAName.setStatus(_A)
_PxmMaRMepAgeOutInterval_Type=Integer32
_PxmMaRMepAgeOutInterval_Object=MibTableColumn
pxmMaRMepAgeOutInterval=_PxmMaRMepAgeOutInterval_Object((1,3,6,1,4,1,21296,2,2,2,2,79,1,1,2),_PxmMaRMepAgeOutInterval_Type())
pxmMaRMepAgeOutInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmMaRMepAgeOutInterval.setStatus(_A)
_PxmMaMDAid_Type=DisplayString
_PxmMaMDAid_Object=MibTableColumn
pxmMaMDAid=_PxmMaMDAid_Object((1,3,6,1,4,1,21296,2,2,2,2,79,1,1,3),_PxmMaMDAid_Type())
pxmMaMDAid.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmMaMDAid.setStatus(_A)
_PxmMaCcmInterval_Type=InfnCcmInterval
_PxmMaCcmInterval_Object=MibTableColumn
pxmMaCcmInterval=_PxmMaCcmInterval_Object((1,3,6,1,4,1,21296,2,2,2,2,79,1,1,4),_PxmMaCcmInterval_Type())
pxmMaCcmInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmMaCcmInterval.setStatus(_A)
_PxmMaMANameFormat_Type=InfnMANameFormat
_PxmMaMANameFormat_Object=MibTableColumn
pxmMaMANameFormat=_PxmMaMANameFormat_Object((1,3,6,1,4,1,21296,2,2,2,2,79,1,1,5),_PxmMaMANameFormat_Type())
pxmMaMANameFormat.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmMaMANameFormat.setStatus(_A)
_PxmMaSenderIDTLV_Type=InfnSenderIDTLV
_PxmMaSenderIDTLV_Object=MibTableColumn
pxmMaSenderIDTLV=_PxmMaSenderIDTLV_Object((1,3,6,1,4,1,21296,2,2,2,2,79,1,1,6),_PxmMaSenderIDTLV_Type())
pxmMaSenderIDTLV.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmMaSenderIDTLV.setStatus(_A)
_PxmMaMDName_Type=DisplayString
_PxmMaMDName_Object=MibTableColumn
pxmMaMDName=_PxmMaMDName_Object((1,3,6,1,4,1,21296,2,2,2,2,79,1,1,7),_PxmMaMDName_Type())
pxmMaMDName.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmMaMDName.setStatus(_A)
_PxmMaMDLevel_Type=Integer32
_PxmMaMDLevel_Object=MibTableColumn
pxmMaMDLevel=_PxmMaMDLevel_Object((1,3,6,1,4,1,21296,2,2,2,2,79,1,1,8),_PxmMaMDLevel_Type())
pxmMaMDLevel.setMaxAccess(_D)
if mibBuilder.loadTexts:pxmMaMDLevel.setStatus(_A)
_PxmMaConformance_ObjectIdentity=ObjectIdentity
pxmMaConformance=_PxmMaConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,79,3))
_PxmMaCompliances_ObjectIdentity=ObjectIdentity
pxmMaCompliances=_PxmMaCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,79,3,1))
_PxmMaGroups_ObjectIdentity=ObjectIdentity
pxmMaGroups=_PxmMaGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,79,3,2))
pxmMaGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,79,3,2,1))
pxmMaGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:pxmMaGroup.setStatus(_A)
pxmMaCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,79,3,1,1))
pxmMaCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:pxmMaCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pxmMaMIB':pxmMaMIB,'pxmMaTable':pxmMaTable,'pxmMaEntry':pxmMaEntry,_G:pxmMaMAName,_H:pxmMaRMepAgeOutInterval,_I:pxmMaMDAid,_J:pxmMaCcmInterval,_K:pxmMaMANameFormat,_L:pxmMaSenderIDTLV,_M:pxmMaMDName,_N:pxmMaMDLevel,'pxmMaConformance':pxmMaConformance,'pxmMaCompliances':pxmMaCompliances,'pxmMaCompliance':pxmMaCompliance,'pxmMaGroups':pxmMaGroups,_O:pxmMaGroup})