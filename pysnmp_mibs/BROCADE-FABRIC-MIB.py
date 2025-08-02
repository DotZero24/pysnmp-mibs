_H='not-accessible'
_G='brcdFabricSfmFeId'
_F='brcdFabricSfmId'
_E='BROCADE-FABRIC-MIB'
_D='snAgentBrdIndex'
_C='FOUNDRY-SN-AGENT-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snAgentBrdIndex,=mibBuilder.importSymbols(_C,_D)
brcdFabric,=mibBuilder.importSymbols('FOUNDRY-SN-ROOT-MIB','brcdFabric')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
brcdFabricMIB=ModuleIdentity((1,3,6,1,4,1,1991,1,1,13,1))
if mibBuilder.loadTexts:brcdFabricMIB.setRevisions(('2012-05-27 00:00',))
_BrcdFabricNotifications_ObjectIdentity=ObjectIdentity
brcdFabricNotifications=_BrcdFabricNotifications_ObjectIdentity((1,3,6,1,4,1,1991,1,1,13,1,0))
_BrcdFabricObjects_ObjectIdentity=ObjectIdentity
brcdFabricObjects=_BrcdFabricObjects_ObjectIdentity((1,3,6,1,4,1,1991,1,1,13,1,1))
_BrcdFabricStatsTable_Object=MibTable
brcdFabricStatsTable=_BrcdFabricStatsTable_Object((1,3,6,1,4,1,1991,1,1,13,1,1,1))
if mibBuilder.loadTexts:brcdFabricStatsTable.setStatus(_A)
_BrcdFabricStatsEntry_Object=MibTableRow
brcdFabricStatsEntry=_BrcdFabricStatsEntry_Object((1,3,6,1,4,1,1991,1,1,13,1,1,1,1))
brcdFabricStatsEntry.setIndexNames((0,_E,_F),(0,_E,_G))
if mibBuilder.loadTexts:brcdFabricStatsEntry.setStatus(_A)
_BrcdFabricSfmId_Type=Unsigned32
_BrcdFabricSfmId_Object=MibTableColumn
brcdFabricSfmId=_BrcdFabricSfmId_Object((1,3,6,1,4,1,1991,1,1,13,1,1,1,1,1),_BrcdFabricSfmId_Type())
brcdFabricSfmId.setMaxAccess(_H)
if mibBuilder.loadTexts:brcdFabricSfmId.setStatus(_A)
_BrcdFabricSfmFeId_Type=Unsigned32
_BrcdFabricSfmFeId_Object=MibTableColumn
brcdFabricSfmFeId=_BrcdFabricSfmFeId_Object((1,3,6,1,4,1,1991,1,1,13,1,1,1,1,2),_BrcdFabricSfmFeId_Type())
brcdFabricSfmFeId.setMaxAccess(_H)
if mibBuilder.loadTexts:brcdFabricSfmFeId.setStatus(_A)
_BrcdFabricDropMAC0Count_Type=Counter32
_BrcdFabricDropMAC0Count_Object=MibTableColumn
brcdFabricDropMAC0Count=_BrcdFabricDropMAC0Count_Object((1,3,6,1,4,1,1991,1,1,13,1,1,1,1,3),_BrcdFabricDropMAC0Count_Type())
brcdFabricDropMAC0Count.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdFabricDropMAC0Count.setStatus(_A)
_BrcdFabricDropMAC1Count_Type=Counter32
_BrcdFabricDropMAC1Count_Object=MibTableColumn
brcdFabricDropMAC1Count=_BrcdFabricDropMAC1Count_Object((1,3,6,1,4,1,1991,1,1,13,1,1,1,1,4),_BrcdFabricDropMAC1Count_Type())
brcdFabricDropMAC1Count.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdFabricDropMAC1Count.setStatus(_A)
_BrcdFabricDropMAC2Count_Type=Counter32
_BrcdFabricDropMAC2Count_Object=MibTableColumn
brcdFabricDropMAC2Count=_BrcdFabricDropMAC2Count_Object((1,3,6,1,4,1,1991,1,1,13,1,1,1,1,5),_BrcdFabricDropMAC2Count_Type())
brcdFabricDropMAC2Count.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdFabricDropMAC2Count.setStatus(_A)
_BrcdFabricDropMAC3Count_Type=Counter32
_BrcdFabricDropMAC3Count_Object=MibTableColumn
brcdFabricDropMAC3Count=_BrcdFabricDropMAC3Count_Object((1,3,6,1,4,1,1991,1,1,13,1,1,1,1,6),_BrcdFabricDropMAC3Count_Type())
brcdFabricDropMAC3Count.setMaxAccess(_B)
if mibBuilder.loadTexts:brcdFabricDropMAC3Count.setStatus(_A)
brcdFabricAutoSFMWalkInitiated=NotificationType((1,3,6,1,4,1,1991,1,1,13,1,0,1))
brcdFabricAutoSFMWalkInitiated.setObjects((_C,_D))
if mibBuilder.loadTexts:brcdFabricAutoSFMWalkInitiated.setStatus(_A)
brcdFabricSFMRemovedFromDatapath=NotificationType((1,3,6,1,4,1,1991,1,1,13,1,0,2))
brcdFabricSFMRemovedFromDatapath.setObjects((_C,_D))
if mibBuilder.loadTexts:brcdFabricSFMRemovedFromDatapath.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'brcdFabricMIB':brcdFabricMIB,'brcdFabricNotifications':brcdFabricNotifications,'brcdFabricAutoSFMWalkInitiated':brcdFabricAutoSFMWalkInitiated,'brcdFabricSFMRemovedFromDatapath':brcdFabricSFMRemovedFromDatapath,'brcdFabricObjects':brcdFabricObjects,'brcdFabricStatsTable':brcdFabricStatsTable,'brcdFabricStatsEntry':brcdFabricStatsEntry,_F:brcdFabricSfmId,_G:brcdFabricSfmFeId,'brcdFabricDropMAC0Count':brcdFabricDropMAC0Count,'brcdFabricDropMAC1Count':brcdFabricDropMAC1Count,'brcdFabricDropMAC2Count':brcdFabricDropMAC2Count,'brcdFabricDropMAC3Count':brcdFabricDropMAC3Count})