_I='bcsiTCAMUsageFeature'
_H='bcsiTCAMUsageProcessor'
_G='bcsiTCAMUsageSlot'
_F='not-accessible'
_E='BROCADE-TCAM-MIB'
_D='Integer32'
_C='Entries'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
bcsiModules,=mibBuilder.importSymbols('Brocade-REG-MIB','bcsiModules')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bcsiTCAM=ModuleIdentity((1,3,6,1,4,1,1588,3,1,14))
if mibBuilder.loadTexts:bcsiTCAM.setRevisions(('2018-05-29 12:00','2016-10-24 13:30'))
_BcsiTCAMNotification_ObjectIdentity=ObjectIdentity
bcsiTCAMNotification=_BcsiTCAMNotification_ObjectIdentity((1,3,6,1,4,1,1588,3,1,14,0))
_BcsiTCAMObjects_ObjectIdentity=ObjectIdentity
bcsiTCAMObjects=_BcsiTCAMObjects_ObjectIdentity((1,3,6,1,4,1,1588,3,1,14,1))
_BcsiTCAMGlobals_ObjectIdentity=ObjectIdentity
bcsiTCAMGlobals=_BcsiTCAMGlobals_ObjectIdentity((1,3,6,1,4,1,1588,3,1,14,1,1))
class _BcsiTCAMProfile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5)));namedValues=NamedValues(*(('default',0),('vxlanExt',1),('l2l3l4Openflow1',2),('l2l3l4Openflow2',3),('v6Openflow1',4),('npbProfile1',5)))
_BcsiTCAMProfile_Type.__name__=_D
_BcsiTCAMProfile_Object=MibScalar
bcsiTCAMProfile=_BcsiTCAMProfile_Object((1,3,6,1,4,1,1588,3,1,14,1,1,1),_BcsiTCAMProfile_Type())
bcsiTCAMProfile.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTCAMProfile.setStatus(_A)
_BcsiTCAMUsageGroup_ObjectIdentity=ObjectIdentity
bcsiTCAMUsageGroup=_BcsiTCAMUsageGroup_ObjectIdentity((1,3,6,1,4,1,1588,3,1,14,1,2))
_BcsiTCAMUsageTable_Object=MibTable
bcsiTCAMUsageTable=_BcsiTCAMUsageTable_Object((1,3,6,1,4,1,1588,3,1,14,1,2,1))
if mibBuilder.loadTexts:bcsiTCAMUsageTable.setStatus(_A)
_BcsiTCAMUsageEntry_Object=MibTableRow
bcsiTCAMUsageEntry=_BcsiTCAMUsageEntry_Object((1,3,6,1,4,1,1588,3,1,14,1,2,1,1))
bcsiTCAMUsageEntry.setIndexNames((0,_E,_G),(0,_E,_H),(0,_E,_I))
if mibBuilder.loadTexts:bcsiTCAMUsageEntry.setStatus(_A)
_BcsiTCAMUsageSlot_Type=Unsigned32
_BcsiTCAMUsageSlot_Object=MibTableColumn
bcsiTCAMUsageSlot=_BcsiTCAMUsageSlot_Object((1,3,6,1,4,1,1588,3,1,14,1,2,1,1,1),_BcsiTCAMUsageSlot_Type())
bcsiTCAMUsageSlot.setMaxAccess(_F)
if mibBuilder.loadTexts:bcsiTCAMUsageSlot.setStatus(_A)
_BcsiTCAMUsageProcessor_Type=Unsigned32
_BcsiTCAMUsageProcessor_Object=MibTableColumn
bcsiTCAMUsageProcessor=_BcsiTCAMUsageProcessor_Object((1,3,6,1,4,1,1588,3,1,14,1,2,1,1,2),_BcsiTCAMUsageProcessor_Type())
bcsiTCAMUsageProcessor.setMaxAccess(_F)
if mibBuilder.loadTexts:bcsiTCAMUsageProcessor.setStatus(_A)
class _BcsiTCAMUsageFeature_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25)));namedValues=NamedValues(*(('l2Ctrl',0),('l3V4Ctrl',1),('l3V6Ctrl',2),('l2UserIngress',3),('l2UserEgress',4),('portRL',5),('bumRL',6),('l3IPV4UserIngress',7),('l3IPV4UserEgress',8),('l3IPV4VxlanVisibility',9),('l3IPV4UserWithRL',10),('l3IPV4RACL',11),('l3IPV4PBR',12),('l3IPV6UserIngress',13),('l3IPV6UserEgress',14),('l3IPV6UserWithRL',15),('l3IPV6RACL',16),('l3IPV6PBR',17),('oflowL2',18),('oflowL3V4',19),('oflowL3V6',20),('oflowL2L3V4',21),('oflowL2L3V6',22),('mct',23),('mplsXC',24),('profileAGT',25)))
_BcsiTCAMUsageFeature_Type.__name__=_D
_BcsiTCAMUsageFeature_Object=MibTableColumn
bcsiTCAMUsageFeature=_BcsiTCAMUsageFeature_Object((1,3,6,1,4,1,1588,3,1,14,1,2,1,1,3),_BcsiTCAMUsageFeature_Type())
bcsiTCAMUsageFeature.setMaxAccess(_F)
if mibBuilder.loadTexts:bcsiTCAMUsageFeature.setStatus(_A)
_BcsiTCAMUsageContainerId_Type=Unsigned32
_BcsiTCAMUsageContainerId_Object=MibTableColumn
bcsiTCAMUsageContainerId=_BcsiTCAMUsageContainerId_Object((1,3,6,1,4,1,1588,3,1,14,1,2,1,1,4),_BcsiTCAMUsageContainerId_Type())
bcsiTCAMUsageContainerId.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTCAMUsageContainerId.setStatus(_A)
_BcsiTCAMUsageDBId_Type=Unsigned32
_BcsiTCAMUsageDBId_Object=MibTableColumn
bcsiTCAMUsageDBId=_BcsiTCAMUsageDBId_Object((1,3,6,1,4,1,1588,3,1,14,1,2,1,1,5),_BcsiTCAMUsageDBId_Type())
bcsiTCAMUsageDBId.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTCAMUsageDBId.setStatus(_A)
class _BcsiTCAMUsageSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('fixed',0),('dynamic',1)))
_BcsiTCAMUsageSize_Type.__name__=_D
_BcsiTCAMUsageSize_Object=MibTableColumn
bcsiTCAMUsageSize=_BcsiTCAMUsageSize_Object((1,3,6,1,4,1,1588,3,1,14,1,2,1,1,6),_BcsiTCAMUsageSize_Type())
bcsiTCAMUsageSize.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTCAMUsageSize.setStatus(_A)
_BcsiTCAMUsageCurrentUsage_Type=Gauge32
_BcsiTCAMUsageCurrentUsage_Object=MibTableColumn
bcsiTCAMUsageCurrentUsage=_BcsiTCAMUsageCurrentUsage_Object((1,3,6,1,4,1,1588,3,1,14,1,2,1,1,7),_BcsiTCAMUsageCurrentUsage_Type())
bcsiTCAMUsageCurrentUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTCAMUsageCurrentUsage.setStatus(_A)
if mibBuilder.loadTexts:bcsiTCAMUsageCurrentUsage.setUnits(_C)
_BcsiTCAMUsageMaxLimit_Type=Gauge32
_BcsiTCAMUsageMaxLimit_Object=MibTableColumn
bcsiTCAMUsageMaxLimit=_BcsiTCAMUsageMaxLimit_Object((1,3,6,1,4,1,1588,3,1,14,1,2,1,1,8),_BcsiTCAMUsageMaxLimit_Type())
bcsiTCAMUsageMaxLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTCAMUsageMaxLimit.setStatus(_A)
if mibBuilder.loadTexts:bcsiTCAMUsageMaxLimit.setUnits(_C)
_BcsiTCAMUsageFreeCountContainer_Type=Gauge32
_BcsiTCAMUsageFreeCountContainer_Object=MibTableColumn
bcsiTCAMUsageFreeCountContainer=_BcsiTCAMUsageFreeCountContainer_Object((1,3,6,1,4,1,1588,3,1,14,1,2,1,1,9),_BcsiTCAMUsageFreeCountContainer_Type())
bcsiTCAMUsageFreeCountContainer.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTCAMUsageFreeCountContainer.setStatus(_A)
if mibBuilder.loadTexts:bcsiTCAMUsageFreeCountContainer.setUnits(_C)
_BcsiTCAMUsageFreeCountDB_Type=Gauge32
_BcsiTCAMUsageFreeCountDB_Object=MibTableColumn
bcsiTCAMUsageFreeCountDB=_BcsiTCAMUsageFreeCountDB_Object((1,3,6,1,4,1,1588,3,1,14,1,2,1,1,10),_BcsiTCAMUsageFreeCountDB_Type())
bcsiTCAMUsageFreeCountDB.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTCAMUsageFreeCountDB.setStatus(_A)
if mibBuilder.loadTexts:bcsiTCAMUsageFreeCountDB.setUnits(_C)
_BcsiTCAMUsageFreeCountFeature_Type=Gauge32
_BcsiTCAMUsageFreeCountFeature_Object=MibTableColumn
bcsiTCAMUsageFreeCountFeature=_BcsiTCAMUsageFreeCountFeature_Object((1,3,6,1,4,1,1588,3,1,14,1,2,1,1,11),_BcsiTCAMUsageFreeCountFeature_Type())
bcsiTCAMUsageFreeCountFeature.setMaxAccess(_B)
if mibBuilder.loadTexts:bcsiTCAMUsageFreeCountFeature.setStatus(_A)
if mibBuilder.loadTexts:bcsiTCAMUsageFreeCountFeature.setUnits(_C)
mibBuilder.exportSymbols(_E,**{'bcsiTCAM':bcsiTCAM,'bcsiTCAMNotification':bcsiTCAMNotification,'bcsiTCAMObjects':bcsiTCAMObjects,'bcsiTCAMGlobals':bcsiTCAMGlobals,'bcsiTCAMProfile':bcsiTCAMProfile,'bcsiTCAMUsageGroup':bcsiTCAMUsageGroup,'bcsiTCAMUsageTable':bcsiTCAMUsageTable,'bcsiTCAMUsageEntry':bcsiTCAMUsageEntry,_G:bcsiTCAMUsageSlot,_H:bcsiTCAMUsageProcessor,_I:bcsiTCAMUsageFeature,'bcsiTCAMUsageContainerId':bcsiTCAMUsageContainerId,'bcsiTCAMUsageDBId':bcsiTCAMUsageDBId,'bcsiTCAMUsageSize':bcsiTCAMUsageSize,'bcsiTCAMUsageCurrentUsage':bcsiTCAMUsageCurrentUsage,'bcsiTCAMUsageMaxLimit':bcsiTCAMUsageMaxLimit,'bcsiTCAMUsageFreeCountContainer':bcsiTCAMUsageFreeCountContainer,'bcsiTCAMUsageFreeCountDB':bcsiTCAMUsageFreeCountDB,'bcsiTCAMUsageFreeCountFeature':bcsiTCAMUsageFreeCountFeature})