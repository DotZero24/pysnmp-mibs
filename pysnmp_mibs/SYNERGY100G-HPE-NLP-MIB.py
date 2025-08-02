_L='syn100GhpeNLPLoopDetectedStatus'
_K='syn100GhpeNLPStatsPortNumber'
_J='syn100GhpeNLPServerPortNumber'
_I='disabled'
_H='enabled'
_G='TruthValue'
_F='Unsigned32'
_E='read-only'
_D='SYNERGY100G-HPE-NLP-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpVCSE_100Gb_F32_Module,=mibBuilder.importSymbols('HPSVRMGMT-OID','hpVCSE-100Gb-F32-Module')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_G)
syn100GhpeNLPMIB=ModuleIdentity((1,3,6,1,4,1,11,5,7,5,9,1,4060))
if mibBuilder.loadTexts:syn100GhpeNLPMIB.setRevisions(('2019-03-05 00:00','2015-07-07 18:31'))
_Syn100GhpeSynergyVCMIBObjects_ObjectIdentity=ObjectIdentity
syn100GhpeSynergyVCMIBObjects=_Syn100GhpeSynergyVCMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,9,1))
class _Syn100GhpeNLPModuleConfig_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_Syn100GhpeNLPModuleConfig_Type.__name__=_B
_Syn100GhpeNLPModuleConfig_Object=MibScalar
syn100GhpeNLPModuleConfig=_Syn100GhpeNLPModuleConfig_Object((1,3,6,1,4,1,11,5,7,5,9,1,4060,1),_Syn100GhpeNLPModuleConfig_Type())
syn100GhpeNLPModuleConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:syn100GhpeNLPModuleConfig.setStatus(_A)
class _Syn100GhpeNLPResetLoopDetection_Type(TruthValue):defaultValue=2
_Syn100GhpeNLPResetLoopDetection_Type.__name__=_G
_Syn100GhpeNLPResetLoopDetection_Object=MibScalar
syn100GhpeNLPResetLoopDetection=_Syn100GhpeNLPResetLoopDetection_Object((1,3,6,1,4,1,11,5,7,5,9,1,4060,2),_Syn100GhpeNLPResetLoopDetection_Type())
syn100GhpeNLPResetLoopDetection.setMaxAccess(_C)
if mibBuilder.loadTexts:syn100GhpeNLPResetLoopDetection.setStatus(_A)
class _Syn100GhpeNLPTransmitInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,10))
_Syn100GhpeNLPTransmitInterval_Type.__name__=_B
_Syn100GhpeNLPTransmitInterval_Object=MibScalar
syn100GhpeNLPTransmitInterval=_Syn100GhpeNLPTransmitInterval_Object((1,3,6,1,4,1,11,5,7,5,9,1,4060,3),_Syn100GhpeNLPTransmitInterval_Type())
syn100GhpeNLPTransmitInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:syn100GhpeNLPTransmitInterval.setStatus(_A)
class _Syn100GhpeNLPEnableTrap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_Syn100GhpeNLPEnableTrap_Type.__name__=_B
_Syn100GhpeNLPEnableTrap_Object=MibScalar
syn100GhpeNLPEnableTrap=_Syn100GhpeNLPEnableTrap_Object((1,3,6,1,4,1,11,5,7,5,9,1,4060,4),_Syn100GhpeNLPEnableTrap_Type())
syn100GhpeNLPEnableTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:syn100GhpeNLPEnableTrap.setStatus(_A)
_Syn100GhpeNLPServerPortTable_Object=MibTable
syn100GhpeNLPServerPortTable=_Syn100GhpeNLPServerPortTable_Object((1,3,6,1,4,1,11,5,7,5,9,1,4060,5))
if mibBuilder.loadTexts:syn100GhpeNLPServerPortTable.setStatus(_A)
_Syn100GhpeNLPServerPortEntry_Object=MibTableRow
syn100GhpeNLPServerPortEntry=_Syn100GhpeNLPServerPortEntry_Object((1,3,6,1,4,1,11,5,7,5,9,1,4060,5,1))
syn100GhpeNLPServerPortEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:syn100GhpeNLPServerPortEntry.setStatus(_A)
class _Syn100GhpeNLPServerPortNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_Syn100GhpeNLPServerPortNumber_Type.__name__=_F
_Syn100GhpeNLPServerPortNumber_Object=MibTableColumn
syn100GhpeNLPServerPortNumber=_Syn100GhpeNLPServerPortNumber_Object((1,3,6,1,4,1,11,5,7,5,9,1,4060,5,1,1),_Syn100GhpeNLPServerPortNumber_Type())
syn100GhpeNLPServerPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:syn100GhpeNLPServerPortNumber.setStatus(_A)
class _Syn100GhpeNLPServerPortResetLoopDetection_Type(TruthValue):defaultValue=2
_Syn100GhpeNLPServerPortResetLoopDetection_Type.__name__=_G
_Syn100GhpeNLPServerPortResetLoopDetection_Object=MibTableColumn
syn100GhpeNLPServerPortResetLoopDetection=_Syn100GhpeNLPServerPortResetLoopDetection_Object((1,3,6,1,4,1,11,5,7,5,9,1,4060,5,1,2),_Syn100GhpeNLPServerPortResetLoopDetection_Type())
syn100GhpeNLPServerPortResetLoopDetection.setMaxAccess(_C)
if mibBuilder.loadTexts:syn100GhpeNLPServerPortResetLoopDetection.setStatus(_A)
class _Syn100GhpeNLPServerPortEnableTrap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_Syn100GhpeNLPServerPortEnableTrap_Type.__name__=_B
_Syn100GhpeNLPServerPortEnableTrap_Object=MibTableColumn
syn100GhpeNLPServerPortEnableTrap=_Syn100GhpeNLPServerPortEnableTrap_Object((1,3,6,1,4,1,11,5,7,5,9,1,4060,5,1,3),_Syn100GhpeNLPServerPortEnableTrap_Type())
syn100GhpeNLPServerPortEnableTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:syn100GhpeNLPServerPortEnableTrap.setStatus(_A)
_Syn100GhpeNLPServerPortStatsTable_Object=MibTable
syn100GhpeNLPServerPortStatsTable=_Syn100GhpeNLPServerPortStatsTable_Object((1,3,6,1,4,1,11,5,7,5,9,1,4060,6))
if mibBuilder.loadTexts:syn100GhpeNLPServerPortStatsTable.setStatus(_A)
_Syn100GhpeNLPServerPortStatsEntry_Object=MibTableRow
syn100GhpeNLPServerPortStatsEntry=_Syn100GhpeNLPServerPortStatsEntry_Object((1,3,6,1,4,1,11,5,7,5,9,1,4060,6,1))
syn100GhpeNLPServerPortStatsEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:syn100GhpeNLPServerPortStatsEntry.setStatus(_A)
class _Syn100GhpeNLPStatsPortNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_Syn100GhpeNLPStatsPortNumber_Type.__name__=_F
_Syn100GhpeNLPStatsPortNumber_Object=MibTableColumn
syn100GhpeNLPStatsPortNumber=_Syn100GhpeNLPStatsPortNumber_Object((1,3,6,1,4,1,11,5,7,5,9,1,4060,6,1,1),_Syn100GhpeNLPStatsPortNumber_Type())
syn100GhpeNLPStatsPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:syn100GhpeNLPStatsPortNumber.setStatus(_A)
class _Syn100GhpeNLPLoopDetectedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_Syn100GhpeNLPLoopDetectedStatus_Type.__name__=_B
_Syn100GhpeNLPLoopDetectedStatus_Object=MibTableColumn
syn100GhpeNLPLoopDetectedStatus=_Syn100GhpeNLPLoopDetectedStatus_Object((1,3,6,1,4,1,11,5,7,5,9,1,4060,6,1,2),_Syn100GhpeNLPLoopDetectedStatus_Type())
syn100GhpeNLPLoopDetectedStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:syn100GhpeNLPLoopDetectedStatus.setStatus(_A)
_Syn100GhpeNLPLoopDetectedCount_Type=Integer32
_Syn100GhpeNLPLoopDetectedCount_Object=MibTableColumn
syn100GhpeNLPLoopDetectedCount=_Syn100GhpeNLPLoopDetectedCount_Object((1,3,6,1,4,1,11,5,7,5,9,1,4060,6,1,3),_Syn100GhpeNLPLoopDetectedCount_Type())
syn100GhpeNLPLoopDetectedCount.setMaxAccess(_E)
if mibBuilder.loadTexts:syn100GhpeNLPLoopDetectedCount.setStatus(_A)
_Syn100GhpeNLPLastLoopDetectTimeStamp_Type=TimeTicks
_Syn100GhpeNLPLastLoopDetectTimeStamp_Object=MibTableColumn
syn100GhpeNLPLastLoopDetectTimeStamp=_Syn100GhpeNLPLastLoopDetectTimeStamp_Object((1,3,6,1,4,1,11,5,7,5,9,1,4060,6,1,4),_Syn100GhpeNLPLastLoopDetectTimeStamp_Type())
syn100GhpeNLPLastLoopDetectTimeStamp.setMaxAccess(_E)
if mibBuilder.loadTexts:syn100GhpeNLPLastLoopDetectTimeStamp.setStatus(_A)
_Syn100Gtraps_ObjectIdentity=ObjectIdentity
syn100Gtraps=_Syn100Gtraps_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,9,1,4060,7))
_Syn100GtrapPrefix_ObjectIdentity=ObjectIdentity
syn100GtrapPrefix=_Syn100GtrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,9,1,4060,7,0))
syn100GhpeNLPLoopDetect=NotificationType((1,3,6,1,4,1,11,5,7,5,9,1,4060,7,0,1))
syn100GhpeNLPLoopDetect.setObjects(*((_D,_J),(_D,_L)))
if mibBuilder.loadTexts:syn100GhpeNLPLoopDetect.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'syn100GhpeSynergyVCMIBObjects':syn100GhpeSynergyVCMIBObjects,'syn100GhpeNLPMIB':syn100GhpeNLPMIB,'syn100GhpeNLPModuleConfig':syn100GhpeNLPModuleConfig,'syn100GhpeNLPResetLoopDetection':syn100GhpeNLPResetLoopDetection,'syn100GhpeNLPTransmitInterval':syn100GhpeNLPTransmitInterval,'syn100GhpeNLPEnableTrap':syn100GhpeNLPEnableTrap,'syn100GhpeNLPServerPortTable':syn100GhpeNLPServerPortTable,'syn100GhpeNLPServerPortEntry':syn100GhpeNLPServerPortEntry,_J:syn100GhpeNLPServerPortNumber,'syn100GhpeNLPServerPortResetLoopDetection':syn100GhpeNLPServerPortResetLoopDetection,'syn100GhpeNLPServerPortEnableTrap':syn100GhpeNLPServerPortEnableTrap,'syn100GhpeNLPServerPortStatsTable':syn100GhpeNLPServerPortStatsTable,'syn100GhpeNLPServerPortStatsEntry':syn100GhpeNLPServerPortStatsEntry,_K:syn100GhpeNLPStatsPortNumber,_L:syn100GhpeNLPLoopDetectedStatus,'syn100GhpeNLPLoopDetectedCount':syn100GhpeNLPLoopDetectedCount,'syn100GhpeNLPLastLoopDetectTimeStamp':syn100GhpeNLPLastLoopDetectTimeStamp,'syn100Gtraps':syn100Gtraps,'syn100GtrapPrefix':syn100GtrapPrefix,'syn100GhpeNLPLoopDetect':syn100GhpeNLPLoopDetect})