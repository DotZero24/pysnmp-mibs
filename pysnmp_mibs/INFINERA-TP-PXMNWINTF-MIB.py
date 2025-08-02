_O='pxmNwIntfGroup'
_N='pxmNwIntfMacAddress'
_M='pxmNwIntfPmHistStatsEnable'
_L='pxmNwIntfAvailableBW'
_K='pxmNwIntfMaxReservableBW'
_J='pxmNwIntfOverbookingFactor'
_I='pxmNwIntfInterfaceRate'
_H='pxmNwIntfMTUSize'
_G='pxmNwIntfAssociatedODUCtp'
_F='read-write'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='INFINERA-TP-PXMNWINTF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
terminationPoint,=mibBuilder.importSymbols('INFINERA-REG-MIB','terminationPoint')
FloatHundredths,FloatTenths,InfnPmHistStatsControl=mibBuilder.importSymbols('INFINERA-TC-MIB','FloatHundredths','FloatTenths','InfnPmHistStatsControl')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pxmNwIntfMIB=ModuleIdentity((1,3,6,1,4,1,21296,2,2,2,2,74))
if mibBuilder.loadTexts:pxmNwIntfMIB.setRevisions(('2016-05-15 00:00',))
_PxmNwIntfTable_Object=MibTable
pxmNwIntfTable=_PxmNwIntfTable_Object((1,3,6,1,4,1,21296,2,2,2,2,74,1))
if mibBuilder.loadTexts:pxmNwIntfTable.setStatus(_A)
_PxmNwIntfEntry_Object=MibTableRow
pxmNwIntfEntry=_PxmNwIntfEntry_Object((1,3,6,1,4,1,21296,2,2,2,2,74,1,1))
pxmNwIntfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:pxmNwIntfEntry.setStatus(_A)
_PxmNwIntfAssociatedODUCtp_Type=DisplayString
_PxmNwIntfAssociatedODUCtp_Object=MibTableColumn
pxmNwIntfAssociatedODUCtp=_PxmNwIntfAssociatedODUCtp_Object((1,3,6,1,4,1,21296,2,2,2,2,74,1,1,1),_PxmNwIntfAssociatedODUCtp_Type())
pxmNwIntfAssociatedODUCtp.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmNwIntfAssociatedODUCtp.setStatus(_A)
_PxmNwIntfMTUSize_Type=Integer32
_PxmNwIntfMTUSize_Object=MibTableColumn
pxmNwIntfMTUSize=_PxmNwIntfMTUSize_Object((1,3,6,1,4,1,21296,2,2,2,2,74,1,1,2),_PxmNwIntfMTUSize_Type())
pxmNwIntfMTUSize.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmNwIntfMTUSize.setStatus(_A)
_PxmNwIntfInterfaceRate_Type=Integer32
_PxmNwIntfInterfaceRate_Object=MibTableColumn
pxmNwIntfInterfaceRate=_PxmNwIntfInterfaceRate_Object((1,3,6,1,4,1,21296,2,2,2,2,74,1,1,3),_PxmNwIntfInterfaceRate_Type())
pxmNwIntfInterfaceRate.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmNwIntfInterfaceRate.setStatus(_A)
_PxmNwIntfOverbookingFactor_Type=FloatTenths
_PxmNwIntfOverbookingFactor_Object=MibTableColumn
pxmNwIntfOverbookingFactor=_PxmNwIntfOverbookingFactor_Object((1,3,6,1,4,1,21296,2,2,2,2,74,1,1,4),_PxmNwIntfOverbookingFactor_Type())
pxmNwIntfOverbookingFactor.setMaxAccess(_F)
if mibBuilder.loadTexts:pxmNwIntfOverbookingFactor.setStatus(_A)
_PxmNwIntfMaxReservableBW_Type=FloatHundredths
_PxmNwIntfMaxReservableBW_Object=MibTableColumn
pxmNwIntfMaxReservableBW=_PxmNwIntfMaxReservableBW_Object((1,3,6,1,4,1,21296,2,2,2,2,74,1,1,5),_PxmNwIntfMaxReservableBW_Type())
pxmNwIntfMaxReservableBW.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmNwIntfMaxReservableBW.setStatus(_A)
_PxmNwIntfAvailableBW_Type=FloatHundredths
_PxmNwIntfAvailableBW_Object=MibTableColumn
pxmNwIntfAvailableBW=_PxmNwIntfAvailableBW_Object((1,3,6,1,4,1,21296,2,2,2,2,74,1,1,6),_PxmNwIntfAvailableBW_Type())
pxmNwIntfAvailableBW.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmNwIntfAvailableBW.setStatus(_A)
_PxmNwIntfPmHistStatsEnable_Type=InfnPmHistStatsControl
_PxmNwIntfPmHistStatsEnable_Object=MibTableColumn
pxmNwIntfPmHistStatsEnable=_PxmNwIntfPmHistStatsEnable_Object((1,3,6,1,4,1,21296,2,2,2,2,74,1,1,7),_PxmNwIntfPmHistStatsEnable_Type())
pxmNwIntfPmHistStatsEnable.setMaxAccess(_F)
if mibBuilder.loadTexts:pxmNwIntfPmHistStatsEnable.setStatus(_A)
_PxmNwIntfMacAddress_Type=DisplayString
_PxmNwIntfMacAddress_Object=MibTableColumn
pxmNwIntfMacAddress=_PxmNwIntfMacAddress_Object((1,3,6,1,4,1,21296,2,2,2,2,74,1,1,8),_PxmNwIntfMacAddress_Type())
pxmNwIntfMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pxmNwIntfMacAddress.setStatus(_A)
_PxmNwIntfConformance_ObjectIdentity=ObjectIdentity
pxmNwIntfConformance=_PxmNwIntfConformance_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,74,3))
_PxmNwIntfCompliances_ObjectIdentity=ObjectIdentity
pxmNwIntfCompliances=_PxmNwIntfCompliances_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,74,3,1))
_PxmNwIntfGroups_ObjectIdentity=ObjectIdentity
pxmNwIntfGroups=_PxmNwIntfGroups_ObjectIdentity((1,3,6,1,4,1,21296,2,2,2,2,74,3,2))
pxmNwIntfGroup=ObjectGroup((1,3,6,1,4,1,21296,2,2,2,2,74,3,2,1))
pxmNwIntfGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:pxmNwIntfGroup.setStatus(_A)
pxmNwIntfCompliance=ModuleCompliance((1,3,6,1,4,1,21296,2,2,2,2,74,3,1,1))
pxmNwIntfCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:pxmNwIntfCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pxmNwIntfMIB':pxmNwIntfMIB,'pxmNwIntfTable':pxmNwIntfTable,'pxmNwIntfEntry':pxmNwIntfEntry,_G:pxmNwIntfAssociatedODUCtp,_H:pxmNwIntfMTUSize,_I:pxmNwIntfInterfaceRate,_J:pxmNwIntfOverbookingFactor,_K:pxmNwIntfMaxReservableBW,_L:pxmNwIntfAvailableBW,_M:pxmNwIntfPmHistStatsEnable,_N:pxmNwIntfMacAddress,'pxmNwIntfConformance':pxmNwIntfConformance,'pxmNwIntfCompliances':pxmNwIntfCompliances,'pxmNwIntfCompliance':pxmNwIntfCompliance,'pxmNwIntfGroups':pxmNwIntfGroups,_O:pxmNwIntfGroup})