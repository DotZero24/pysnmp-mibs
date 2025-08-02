_I='adGenAosY1731Group'
_H='adGenAosY1731Alarms'
_G='adGenAosY1731LocalMepId'
_F='Unsigned32'
_E='dot1agCfmMdIndex'
_D='dot1agCfmMaIndex'
_C='IEEE8021-CFM-MIB'
_B='ADTRAN-AOS-Y1731-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenAOS,adGenAOSConformance,adGenAOSMef=mibBuilder.importSymbols('ADTRAN-AOS','adGenAOS','adGenAOSConformance','adGenAOSMef')
adIdentity,=mibBuilder.importSymbols('ADTRAN-MIB','adIdentity')
dot1agCfmMaIndex,dot1agCfmMdIndex=mibBuilder.importSymbols(_C,_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenAosY1731Mib=ModuleIdentity((1,3,6,1,4,1,664,6,10000,53,9,9))
class AdGenAosY1731Alarms(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('bDefY1731CcmRxRDIAlarm',0),('bDefY1731CcmLossOfContinuityAlarm',1),('bDefY1731CcmUnexpectedMepAlarm',2),('bDefY1731CcmUnexpectedPeriodAlarm',3),('bDefY1731CcmMismergeAlarm',4),('bDefY1731CcmUnexpectedMegLevelAlarm',5)))
_AdGenAosY1731_ObjectIdentity=ObjectIdentity
adGenAosY1731=_AdGenAosY1731_ObjectIdentity((1,3,6,1,4,1,664,5,53,9,9))
_AdGenAosY1731LocalMepTable_Object=MibTable
adGenAosY1731LocalMepTable=_AdGenAosY1731LocalMepTable_Object((1,3,6,1,4,1,664,5,53,9,9,1))
if mibBuilder.loadTexts:adGenAosY1731LocalMepTable.setStatus(_A)
_AdGenAosY1731LocalMepEntry_Object=MibTableRow
adGenAosY1731LocalMepEntry=_AdGenAosY1731LocalMepEntry_Object((1,3,6,1,4,1,664,5,53,9,9,1,1))
adGenAosY1731LocalMepEntry.setIndexNames((0,_C,_E),(0,_C,_D),(0,_B,_G))
if mibBuilder.loadTexts:adGenAosY1731LocalMepEntry.setStatus(_A)
class _AdGenAosY1731LocalMepId_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8191))
_AdGenAosY1731LocalMepId_Type.__name__=_F
_AdGenAosY1731LocalMepId_Object=MibTableColumn
adGenAosY1731LocalMepId=_AdGenAosY1731LocalMepId_Object((1,3,6,1,4,1,664,5,53,9,9,1,1,1),_AdGenAosY1731LocalMepId_Type())
adGenAosY1731LocalMepId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:adGenAosY1731LocalMepId.setStatus(_A)
_AdGenAosY1731Alarms_Type=AdGenAosY1731Alarms
_AdGenAosY1731Alarms_Object=MibTableColumn
adGenAosY1731Alarms=_AdGenAosY1731Alarms_Object((1,3,6,1,4,1,664,5,53,9,9,1,1,2),_AdGenAosY1731Alarms_Type())
adGenAosY1731Alarms.setMaxAccess('read-only')
if mibBuilder.loadTexts:adGenAosY1731Alarms.setStatus(_A)
_AdGenAosY1731Conformance_ObjectIdentity=ObjectIdentity
adGenAosY1731Conformance=_AdGenAosY1731Conformance_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,34))
_AdGenAosY1731Groups_ObjectIdentity=ObjectIdentity
adGenAosY1731Groups=_AdGenAosY1731Groups_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,34,1))
_AdGenAosY1731Compliances_ObjectIdentity=ObjectIdentity
adGenAosY1731Compliances=_AdGenAosY1731Compliances_ObjectIdentity((1,3,6,1,4,1,664,5,53,99,34,2))
adGenAosY1731Group=ObjectGroup((1,3,6,1,4,1,664,5,53,99,34,1,1))
adGenAosY1731Group.setObjects((_B,_H))
if mibBuilder.loadTexts:adGenAosY1731Group.setStatus(_A)
adGenAosY1731FullCompliance=ModuleCompliance((1,3,6,1,4,1,664,5,53,99,34,2,1))
adGenAosY1731FullCompliance.setObjects((_B,_I))
if mibBuilder.loadTexts:adGenAosY1731FullCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'AdGenAosY1731Alarms':AdGenAosY1731Alarms,'adGenAosY1731':adGenAosY1731,'adGenAosY1731LocalMepTable':adGenAosY1731LocalMepTable,'adGenAosY1731LocalMepEntry':adGenAosY1731LocalMepEntry,_G:adGenAosY1731LocalMepId,_H:adGenAosY1731Alarms,'adGenAosY1731Conformance':adGenAosY1731Conformance,'adGenAosY1731Groups':adGenAosY1731Groups,_I:adGenAosY1731Group,'adGenAosY1731Compliances':adGenAosY1731Compliances,'adGenAosY1731FullCompliance':adGenAosY1731FullCompliance,'adGenAosY1731Mib':adGenAosY1731Mib})