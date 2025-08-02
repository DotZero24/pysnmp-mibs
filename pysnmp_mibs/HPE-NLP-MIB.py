_L='hpeNLPLoopDetectedStatus'
_K='hpeNLPStatsPortNumber'
_J='hpeNLPServerPortNumber'
_I='disabled'
_H='enabled'
_G='TruthValue'
_F='Unsigned32'
_E='read-only'
_D='HPE-NLP-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpVCSE_40Gb_F8_Module,=mibBuilder.importSymbols('HPSVRMGMT-OID','hpVCSE-40Gb-F8-Module')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'enterprises','iso')
DisplayString,PhysAddress,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TimeStamp',_G)
hpeNLPMIB=ModuleIdentity((1,3,6,1,4,1,11,5,7,5,8,1,4060))
if mibBuilder.loadTexts:hpeNLPMIB.setRevisions(('2019-03-05 00:00','2015-07-07 18:31'))
_HpeSynergyVCMIBObjects_ObjectIdentity=ObjectIdentity
hpeSynergyVCMIBObjects=_HpeSynergyVCMIBObjects_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,8,1))
class _HpeNLPModuleConfig_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HpeNLPModuleConfig_Type.__name__=_B
_HpeNLPModuleConfig_Object=MibScalar
hpeNLPModuleConfig=_HpeNLPModuleConfig_Object((1,3,6,1,4,1,11,5,7,5,8,1,4060,1),_HpeNLPModuleConfig_Type())
hpeNLPModuleConfig.setMaxAccess(_C)
if mibBuilder.loadTexts:hpeNLPModuleConfig.setStatus(_A)
class _HpeNLPResetLoopDetection_Type(TruthValue):defaultValue=2
_HpeNLPResetLoopDetection_Type.__name__=_G
_HpeNLPResetLoopDetection_Object=MibScalar
hpeNLPResetLoopDetection=_HpeNLPResetLoopDetection_Object((1,3,6,1,4,1,11,5,7,5,8,1,4060,2),_HpeNLPResetLoopDetection_Type())
hpeNLPResetLoopDetection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpeNLPResetLoopDetection.setStatus(_A)
class _HpeNLPTransmitInterval_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(5,10))
_HpeNLPTransmitInterval_Type.__name__=_B
_HpeNLPTransmitInterval_Object=MibScalar
hpeNLPTransmitInterval=_HpeNLPTransmitInterval_Object((1,3,6,1,4,1,11,5,7,5,8,1,4060,3),_HpeNLPTransmitInterval_Type())
hpeNLPTransmitInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:hpeNLPTransmitInterval.setStatus(_A)
class _HpeNLPEnableTrap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HpeNLPEnableTrap_Type.__name__=_B
_HpeNLPEnableTrap_Object=MibScalar
hpeNLPEnableTrap=_HpeNLPEnableTrap_Object((1,3,6,1,4,1,11,5,7,5,8,1,4060,4),_HpeNLPEnableTrap_Type())
hpeNLPEnableTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:hpeNLPEnableTrap.setStatus(_A)
_HpeNLPServerPortTable_Object=MibTable
hpeNLPServerPortTable=_HpeNLPServerPortTable_Object((1,3,6,1,4,1,11,5,7,5,8,1,4060,5))
if mibBuilder.loadTexts:hpeNLPServerPortTable.setStatus(_A)
_HpeNLPServerPortEntry_Object=MibTableRow
hpeNLPServerPortEntry=_HpeNLPServerPortEntry_Object((1,3,6,1,4,1,11,5,7,5,8,1,4060,5,1))
hpeNLPServerPortEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:hpeNLPServerPortEntry.setStatus(_A)
class _HpeNLPServerPortNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_HpeNLPServerPortNumber_Type.__name__=_F
_HpeNLPServerPortNumber_Object=MibTableColumn
hpeNLPServerPortNumber=_HpeNLPServerPortNumber_Object((1,3,6,1,4,1,11,5,7,5,8,1,4060,5,1,1),_HpeNLPServerPortNumber_Type())
hpeNLPServerPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hpeNLPServerPortNumber.setStatus(_A)
class _HpeNLPServerPortResetLoopDetection_Type(TruthValue):defaultValue=2
_HpeNLPServerPortResetLoopDetection_Type.__name__=_G
_HpeNLPServerPortResetLoopDetection_Object=MibTableColumn
hpeNLPServerPortResetLoopDetection=_HpeNLPServerPortResetLoopDetection_Object((1,3,6,1,4,1,11,5,7,5,8,1,4060,5,1,2),_HpeNLPServerPortResetLoopDetection_Type())
hpeNLPServerPortResetLoopDetection.setMaxAccess(_C)
if mibBuilder.loadTexts:hpeNLPServerPortResetLoopDetection.setStatus(_A)
class _HpeNLPServerPortEnableTrap_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_HpeNLPServerPortEnableTrap_Type.__name__=_B
_HpeNLPServerPortEnableTrap_Object=MibTableColumn
hpeNLPServerPortEnableTrap=_HpeNLPServerPortEnableTrap_Object((1,3,6,1,4,1,11,5,7,5,8,1,4060,5,1,3),_HpeNLPServerPortEnableTrap_Type())
hpeNLPServerPortEnableTrap.setMaxAccess(_C)
if mibBuilder.loadTexts:hpeNLPServerPortEnableTrap.setStatus(_A)
_HpeNLPServerPortStats_Object=MibTable
hpeNLPServerPortStats=_HpeNLPServerPortStats_Object((1,3,6,1,4,1,11,5,7,5,8,1,4060,6))
if mibBuilder.loadTexts:hpeNLPServerPortStats.setStatus(_A)
_HpeNLPServerPortStatsEntry_Object=MibTableRow
hpeNLPServerPortStatsEntry=_HpeNLPServerPortStatsEntry_Object((1,3,6,1,4,1,11,5,7,5,8,1,4060,6,1))
hpeNLPServerPortStatsEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:hpeNLPServerPortStatsEntry.setStatus(_A)
class _HpeNLPStatsPortNumber_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,60))
_HpeNLPStatsPortNumber_Type.__name__=_F
_HpeNLPStatsPortNumber_Object=MibTableColumn
hpeNLPStatsPortNumber=_HpeNLPStatsPortNumber_Object((1,3,6,1,4,1,11,5,7,5,8,1,4060,6,1,1),_HpeNLPStatsPortNumber_Type())
hpeNLPStatsPortNumber.setMaxAccess(_E)
if mibBuilder.loadTexts:hpeNLPStatsPortNumber.setStatus(_A)
class _HpeNLPLoopDetectedStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('yes',1),('no',2)))
_HpeNLPLoopDetectedStatus_Type.__name__=_B
_HpeNLPLoopDetectedStatus_Object=MibTableColumn
hpeNLPLoopDetectedStatus=_HpeNLPLoopDetectedStatus_Object((1,3,6,1,4,1,11,5,7,5,8,1,4060,6,1,2),_HpeNLPLoopDetectedStatus_Type())
hpeNLPLoopDetectedStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:hpeNLPLoopDetectedStatus.setStatus(_A)
_HpeNLPLoopDetectedCount_Type=Integer32
_HpeNLPLoopDetectedCount_Object=MibTableColumn
hpeNLPLoopDetectedCount=_HpeNLPLoopDetectedCount_Object((1,3,6,1,4,1,11,5,7,5,8,1,4060,6,1,3),_HpeNLPLoopDetectedCount_Type())
hpeNLPLoopDetectedCount.setMaxAccess(_E)
if mibBuilder.loadTexts:hpeNLPLoopDetectedCount.setStatus(_A)
_HpeNLPLastLoopDetectTimeStamp_Type=TimeTicks
_HpeNLPLastLoopDetectTimeStamp_Object=MibTableColumn
hpeNLPLastLoopDetectTimeStamp=_HpeNLPLastLoopDetectTimeStamp_Object((1,3,6,1,4,1,11,5,7,5,8,1,4060,6,1,4),_HpeNLPLastLoopDetectTimeStamp_Type())
hpeNLPLastLoopDetectTimeStamp.setMaxAccess(_E)
if mibBuilder.loadTexts:hpeNLPLastLoopDetectTimeStamp.setStatus(_A)
_Traps_ObjectIdentity=ObjectIdentity
traps=_Traps_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,8,1,4060,7))
_TrapPrefix_ObjectIdentity=ObjectIdentity
trapPrefix=_TrapPrefix_ObjectIdentity((1,3,6,1,4,1,11,5,7,5,8,1,4060,7,0))
hpeNLPLoopDetect=NotificationType((1,3,6,1,4,1,11,5,7,5,8,1,4060,7,0,1))
hpeNLPLoopDetect.setObjects(*((_D,_J),(_D,_L)))
if mibBuilder.loadTexts:hpeNLPLoopDetect.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'hpeSynergyVCMIBObjects':hpeSynergyVCMIBObjects,'hpeNLPMIB':hpeNLPMIB,'hpeNLPModuleConfig':hpeNLPModuleConfig,'hpeNLPResetLoopDetection':hpeNLPResetLoopDetection,'hpeNLPTransmitInterval':hpeNLPTransmitInterval,'hpeNLPEnableTrap':hpeNLPEnableTrap,'hpeNLPServerPortTable':hpeNLPServerPortTable,'hpeNLPServerPortEntry':hpeNLPServerPortEntry,_J:hpeNLPServerPortNumber,'hpeNLPServerPortResetLoopDetection':hpeNLPServerPortResetLoopDetection,'hpeNLPServerPortEnableTrap':hpeNLPServerPortEnableTrap,'hpeNLPServerPortStats':hpeNLPServerPortStats,'hpeNLPServerPortStatsEntry':hpeNLPServerPortStatsEntry,_K:hpeNLPStatsPortNumber,_L:hpeNLPLoopDetectedStatus,'hpeNLPLoopDetectedCount':hpeNLPLoopDetectedCount,'hpeNLPLastLoopDetectTimeStamp':hpeNLPLastLoopDetectTimeStamp,'traps':traps,'trapPrefix':trapPrefix,'hpeNLPLoopDetect':hpeNLPLoopDetect})