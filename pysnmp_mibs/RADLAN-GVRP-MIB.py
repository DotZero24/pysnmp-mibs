_K='passive'
_J='activate'
_I='TruthValue'
_H='EnabledStatus'
_G='TimeInterval'
_F='Integer32'
_E='dot1dBasePort'
_D='BRIDGE-MIB'
_C='read-write'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_D,_E)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB',_H)
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TimeInterval,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_G,_I)
rlGvrp=ModuleIdentity((1,3,6,1,4,1,89,64))
if mibBuilder.loadTexts:rlGvrp.setRevisions(('2007-01-02 00:00',))
_RlPortGvrpTimersTable_Object=MibTable
rlPortGvrpTimersTable=_RlPortGvrpTimersTable_Object((1,3,6,1,4,1,89,64,1))
if mibBuilder.loadTexts:rlPortGvrpTimersTable.setStatus(_A)
_RlPortGvrpTimersEntry_Object=MibTableRow
rlPortGvrpTimersEntry=_RlPortGvrpTimersEntry_Object((1,3,6,1,4,1,89,64,1,1))
rlPortGvrpTimersEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlPortGvrpTimersEntry.setStatus(_A)
class _RlPortGvrpJoinTime_Type(TimeInterval):defaultValue=20
_RlPortGvrpJoinTime_Type.__name__=_G
_RlPortGvrpJoinTime_Object=MibTableColumn
rlPortGvrpJoinTime=_RlPortGvrpJoinTime_Object((1,3,6,1,4,1,89,64,1,1,1),_RlPortGvrpJoinTime_Type())
rlPortGvrpJoinTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPortGvrpJoinTime.setStatus(_A)
class _RlPortGvrpLeaveTime_Type(TimeInterval):defaultValue=60
_RlPortGvrpLeaveTime_Type.__name__=_G
_RlPortGvrpLeaveTime_Object=MibTableColumn
rlPortGvrpLeaveTime=_RlPortGvrpLeaveTime_Object((1,3,6,1,4,1,89,64,1,1,2),_RlPortGvrpLeaveTime_Type())
rlPortGvrpLeaveTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPortGvrpLeaveTime.setStatus(_A)
class _RlPortGvrpLeaveAllTime_Type(TimeInterval):defaultValue=1000
_RlPortGvrpLeaveAllTime_Type.__name__=_G
_RlPortGvrpLeaveAllTime_Object=MibTableColumn
rlPortGvrpLeaveAllTime=_RlPortGvrpLeaveAllTime_Object((1,3,6,1,4,1,89,64,1,1,3),_RlPortGvrpLeaveAllTime_Type())
rlPortGvrpLeaveAllTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPortGvrpLeaveAllTime.setStatus(_A)
class _RlPortGvrpOverrideGarp_Type(EnabledStatus):defaultValue=2
_RlPortGvrpOverrideGarp_Type.__name__=_H
_RlPortGvrpOverrideGarp_Object=MibTableColumn
rlPortGvrpOverrideGarp=_RlPortGvrpOverrideGarp_Object((1,3,6,1,4,1,89,64,1,1,4),_RlPortGvrpOverrideGarp_Type())
rlPortGvrpOverrideGarp.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPortGvrpOverrideGarp.setStatus(_A)
_RlGvrpSupported_Type=TruthValue
_RlGvrpSupported_Object=MibScalar
rlGvrpSupported=_RlGvrpSupported_Object((1,3,6,1,4,1,89,64,2),_RlGvrpSupported_Type())
rlGvrpSupported.setMaxAccess(_B)
if mibBuilder.loadTexts:rlGvrpSupported.setStatus(_A)
_RlGvrpMibVersion_Type=Integer32
_RlGvrpMibVersion_Object=MibScalar
rlGvrpMibVersion=_RlGvrpMibVersion_Object((1,3,6,1,4,1,89,64,3),_RlGvrpMibVersion_Type())
rlGvrpMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:rlGvrpMibVersion.setStatus(_A)
_RlPortGvrpStatisticsTable_Object=MibTable
rlPortGvrpStatisticsTable=_RlPortGvrpStatisticsTable_Object((1,3,6,1,4,1,89,64,4))
if mibBuilder.loadTexts:rlPortGvrpStatisticsTable.setStatus(_A)
_RlPortGvrpStatisticsEntry_Object=MibTableRow
rlPortGvrpStatisticsEntry=_RlPortGvrpStatisticsEntry_Object((1,3,6,1,4,1,89,64,4,1))
rlPortGvrpStatisticsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlPortGvrpStatisticsEntry.setStatus(_A)
_RlPortGvrpStatisticsRJE_Type=Counter32
_RlPortGvrpStatisticsRJE_Object=MibTableColumn
rlPortGvrpStatisticsRJE=_RlPortGvrpStatisticsRJE_Object((1,3,6,1,4,1,89,64,4,1,1),_RlPortGvrpStatisticsRJE_Type())
rlPortGvrpStatisticsRJE.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpStatisticsRJE.setStatus(_A)
_RlPortGvrpStatisticsRJIn_Type=Counter32
_RlPortGvrpStatisticsRJIn_Object=MibTableColumn
rlPortGvrpStatisticsRJIn=_RlPortGvrpStatisticsRJIn_Object((1,3,6,1,4,1,89,64,4,1,2),_RlPortGvrpStatisticsRJIn_Type())
rlPortGvrpStatisticsRJIn.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpStatisticsRJIn.setStatus(_A)
_RlPortGvrpStatisticsREmp_Type=Counter32
_RlPortGvrpStatisticsREmp_Object=MibTableColumn
rlPortGvrpStatisticsREmp=_RlPortGvrpStatisticsREmp_Object((1,3,6,1,4,1,89,64,4,1,3),_RlPortGvrpStatisticsREmp_Type())
rlPortGvrpStatisticsREmp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpStatisticsREmp.setStatus(_A)
_RlPortGvrpStatisticsRLIn_Type=Counter32
_RlPortGvrpStatisticsRLIn_Object=MibTableColumn
rlPortGvrpStatisticsRLIn=_RlPortGvrpStatisticsRLIn_Object((1,3,6,1,4,1,89,64,4,1,4),_RlPortGvrpStatisticsRLIn_Type())
rlPortGvrpStatisticsRLIn.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpStatisticsRLIn.setStatus(_A)
_RlPortGvrpStatisticsRLE_Type=Counter32
_RlPortGvrpStatisticsRLE_Object=MibTableColumn
rlPortGvrpStatisticsRLE=_RlPortGvrpStatisticsRLE_Object((1,3,6,1,4,1,89,64,4,1,5),_RlPortGvrpStatisticsRLE_Type())
rlPortGvrpStatisticsRLE.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpStatisticsRLE.setStatus(_A)
_RlPortGvrpStatisticsRLA_Type=Counter32
_RlPortGvrpStatisticsRLA_Object=MibTableColumn
rlPortGvrpStatisticsRLA=_RlPortGvrpStatisticsRLA_Object((1,3,6,1,4,1,89,64,4,1,6),_RlPortGvrpStatisticsRLA_Type())
rlPortGvrpStatisticsRLA.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpStatisticsRLA.setStatus(_A)
_RlPortGvrpStatisticsSJE_Type=Counter32
_RlPortGvrpStatisticsSJE_Object=MibTableColumn
rlPortGvrpStatisticsSJE=_RlPortGvrpStatisticsSJE_Object((1,3,6,1,4,1,89,64,4,1,7),_RlPortGvrpStatisticsSJE_Type())
rlPortGvrpStatisticsSJE.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpStatisticsSJE.setStatus(_A)
_RlPortGvrpStatisticsSJIn_Type=Counter32
_RlPortGvrpStatisticsSJIn_Object=MibTableColumn
rlPortGvrpStatisticsSJIn=_RlPortGvrpStatisticsSJIn_Object((1,3,6,1,4,1,89,64,4,1,8),_RlPortGvrpStatisticsSJIn_Type())
rlPortGvrpStatisticsSJIn.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpStatisticsSJIn.setStatus(_A)
_RlPortGvrpStatisticsSEmp_Type=Counter32
_RlPortGvrpStatisticsSEmp_Object=MibTableColumn
rlPortGvrpStatisticsSEmp=_RlPortGvrpStatisticsSEmp_Object((1,3,6,1,4,1,89,64,4,1,9),_RlPortGvrpStatisticsSEmp_Type())
rlPortGvrpStatisticsSEmp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpStatisticsSEmp.setStatus(_A)
_RlPortGvrpStatisticsSLIn_Type=Counter32
_RlPortGvrpStatisticsSLIn_Object=MibTableColumn
rlPortGvrpStatisticsSLIn=_RlPortGvrpStatisticsSLIn_Object((1,3,6,1,4,1,89,64,4,1,10),_RlPortGvrpStatisticsSLIn_Type())
rlPortGvrpStatisticsSLIn.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpStatisticsSLIn.setStatus(_A)
_RlPortGvrpStatisticsSLE_Type=Counter32
_RlPortGvrpStatisticsSLE_Object=MibTableColumn
rlPortGvrpStatisticsSLE=_RlPortGvrpStatisticsSLE_Object((1,3,6,1,4,1,89,64,4,1,11),_RlPortGvrpStatisticsSLE_Type())
rlPortGvrpStatisticsSLE.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpStatisticsSLE.setStatus(_A)
_RlPortGvrpStatisticsSLA_Type=Counter32
_RlPortGvrpStatisticsSLA_Object=MibTableColumn
rlPortGvrpStatisticsSLA=_RlPortGvrpStatisticsSLA_Object((1,3,6,1,4,1,89,64,4,1,12),_RlPortGvrpStatisticsSLA_Type())
rlPortGvrpStatisticsSLA.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpStatisticsSLA.setStatus(_A)
class _RlPortGvrpStatisticsClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_RlPortGvrpStatisticsClear_Type.__name__=_F
_RlPortGvrpStatisticsClear_Object=MibTableColumn
rlPortGvrpStatisticsClear=_RlPortGvrpStatisticsClear_Object((1,3,6,1,4,1,89,64,4,1,13),_RlPortGvrpStatisticsClear_Type())
rlPortGvrpStatisticsClear.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPortGvrpStatisticsClear.setStatus(_A)
_RlPortGvrpErrorStatisticsTable_Object=MibTable
rlPortGvrpErrorStatisticsTable=_RlPortGvrpErrorStatisticsTable_Object((1,3,6,1,4,1,89,64,5))
if mibBuilder.loadTexts:rlPortGvrpErrorStatisticsTable.setStatus(_A)
_RlPortGvrpErrorStatisticsEntry_Object=MibTableRow
rlPortGvrpErrorStatisticsEntry=_RlPortGvrpErrorStatisticsEntry_Object((1,3,6,1,4,1,89,64,5,1))
rlPortGvrpErrorStatisticsEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlPortGvrpErrorStatisticsEntry.setStatus(_A)
_RlPortGvrpErrorStatisticsInvProt_Type=Counter32
_RlPortGvrpErrorStatisticsInvProt_Object=MibTableColumn
rlPortGvrpErrorStatisticsInvProt=_RlPortGvrpErrorStatisticsInvProt_Object((1,3,6,1,4,1,89,64,5,1,1),_RlPortGvrpErrorStatisticsInvProt_Type())
rlPortGvrpErrorStatisticsInvProt.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpErrorStatisticsInvProt.setStatus(_A)
_RlPortGvrpErrorStatisticsInvAtyp_Type=Counter32
_RlPortGvrpErrorStatisticsInvAtyp_Object=MibTableColumn
rlPortGvrpErrorStatisticsInvAtyp=_RlPortGvrpErrorStatisticsInvAtyp_Object((1,3,6,1,4,1,89,64,5,1,2),_RlPortGvrpErrorStatisticsInvAtyp_Type())
rlPortGvrpErrorStatisticsInvAtyp.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpErrorStatisticsInvAtyp.setStatus(_A)
_RlPortGvrpErrorStatisticsInvAval_Type=Counter32
_RlPortGvrpErrorStatisticsInvAval_Object=MibTableColumn
rlPortGvrpErrorStatisticsInvAval=_RlPortGvrpErrorStatisticsInvAval_Object((1,3,6,1,4,1,89,64,5,1,3),_RlPortGvrpErrorStatisticsInvAval_Type())
rlPortGvrpErrorStatisticsInvAval.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpErrorStatisticsInvAval.setStatus(_A)
_RlPortGvrpErrorStatisticsInvPlen_Type=Counter32
_RlPortGvrpErrorStatisticsInvPlen_Object=MibTableColumn
rlPortGvrpErrorStatisticsInvPlen=_RlPortGvrpErrorStatisticsInvPlen_Object((1,3,6,1,4,1,89,64,5,1,4),_RlPortGvrpErrorStatisticsInvPlen_Type())
rlPortGvrpErrorStatisticsInvPlen.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpErrorStatisticsInvPlen.setStatus(_A)
_RlPortGvrpErrorStatisticsInvAlen_Type=Counter32
_RlPortGvrpErrorStatisticsInvAlen_Object=MibTableColumn
rlPortGvrpErrorStatisticsInvAlen=_RlPortGvrpErrorStatisticsInvAlen_Object((1,3,6,1,4,1,89,64,5,1,5),_RlPortGvrpErrorStatisticsInvAlen_Type())
rlPortGvrpErrorStatisticsInvAlen.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpErrorStatisticsInvAlen.setStatus(_A)
_RlPortGvrpErrorStatisticsInvEvent_Type=Counter32
_RlPortGvrpErrorStatisticsInvEvent_Object=MibTableColumn
rlPortGvrpErrorStatisticsInvEvent=_RlPortGvrpErrorStatisticsInvEvent_Object((1,3,6,1,4,1,89,64,5,1,6),_RlPortGvrpErrorStatisticsInvEvent_Type())
rlPortGvrpErrorStatisticsInvEvent.setMaxAccess(_B)
if mibBuilder.loadTexts:rlPortGvrpErrorStatisticsInvEvent.setStatus(_A)
class _RlPortGvrpErrorStatisticsClear_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_J,1),(_K,2)))
_RlPortGvrpErrorStatisticsClear_Type.__name__=_F
_RlPortGvrpErrorStatisticsClear_Object=MibTableColumn
rlPortGvrpErrorStatisticsClear=_RlPortGvrpErrorStatisticsClear_Object((1,3,6,1,4,1,89,64,5,1,7),_RlPortGvrpErrorStatisticsClear_Type())
rlPortGvrpErrorStatisticsClear.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPortGvrpErrorStatisticsClear.setStatus(_A)
_RlPortGvrpApplicantStatusTable_Object=MibTable
rlPortGvrpApplicantStatusTable=_RlPortGvrpApplicantStatusTable_Object((1,3,6,1,4,1,89,64,6))
if mibBuilder.loadTexts:rlPortGvrpApplicantStatusTable.setStatus(_A)
_RlPortGvrpApplicantStatusEntry_Object=MibTableRow
rlPortGvrpApplicantStatusEntry=_RlPortGvrpApplicantStatusEntry_Object((1,3,6,1,4,1,89,64,6,1))
rlPortGvrpApplicantStatusEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlPortGvrpApplicantStatusEntry.setStatus(_A)
class _RlPortGvrpApplicantStatusValue_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('participant',1),('nonParticipant',2)))
_RlPortGvrpApplicantStatusValue_Type.__name__=_F
_RlPortGvrpApplicantStatusValue_Object=MibTableColumn
rlPortGvrpApplicantStatusValue=_RlPortGvrpApplicantStatusValue_Object((1,3,6,1,4,1,89,64,6,1,1),_RlPortGvrpApplicantStatusValue_Type())
rlPortGvrpApplicantStatusValue.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPortGvrpApplicantStatusValue.setStatus(_A)
_RlPortGvrpRegistrationModeTable_Object=MibTable
rlPortGvrpRegistrationModeTable=_RlPortGvrpRegistrationModeTable_Object((1,3,6,1,4,1,89,64,8))
if mibBuilder.loadTexts:rlPortGvrpRegistrationModeTable.setStatus(_A)
_RlPortGvrpRegistrationModeEntry_Object=MibTableRow
rlPortGvrpRegistrationModeEntry=_RlPortGvrpRegistrationModeEntry_Object((1,3,6,1,4,1,89,64,8,1))
rlPortGvrpRegistrationModeEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:rlPortGvrpRegistrationModeEntry.setStatus(_A)
class _RlPortGvrpRegistrationModeForbidden_Type(TruthValue):defaultValue=2
_RlPortGvrpRegistrationModeForbidden_Type.__name__=_I
_RlPortGvrpRegistrationModeForbidden_Object=MibTableColumn
rlPortGvrpRegistrationModeForbidden=_RlPortGvrpRegistrationModeForbidden_Object((1,3,6,1,4,1,89,64,8,1,1),_RlPortGvrpRegistrationModeForbidden_Type())
rlPortGvrpRegistrationModeForbidden.setMaxAccess(_C)
if mibBuilder.loadTexts:rlPortGvrpRegistrationModeForbidden.setStatus(_A)
mibBuilder.exportSymbols('RADLAN-GVRP-MIB',**{'rlGvrp':rlGvrp,'rlPortGvrpTimersTable':rlPortGvrpTimersTable,'rlPortGvrpTimersEntry':rlPortGvrpTimersEntry,'rlPortGvrpJoinTime':rlPortGvrpJoinTime,'rlPortGvrpLeaveTime':rlPortGvrpLeaveTime,'rlPortGvrpLeaveAllTime':rlPortGvrpLeaveAllTime,'rlPortGvrpOverrideGarp':rlPortGvrpOverrideGarp,'rlGvrpSupported':rlGvrpSupported,'rlGvrpMibVersion':rlGvrpMibVersion,'rlPortGvrpStatisticsTable':rlPortGvrpStatisticsTable,'rlPortGvrpStatisticsEntry':rlPortGvrpStatisticsEntry,'rlPortGvrpStatisticsRJE':rlPortGvrpStatisticsRJE,'rlPortGvrpStatisticsRJIn':rlPortGvrpStatisticsRJIn,'rlPortGvrpStatisticsREmp':rlPortGvrpStatisticsREmp,'rlPortGvrpStatisticsRLIn':rlPortGvrpStatisticsRLIn,'rlPortGvrpStatisticsRLE':rlPortGvrpStatisticsRLE,'rlPortGvrpStatisticsRLA':rlPortGvrpStatisticsRLA,'rlPortGvrpStatisticsSJE':rlPortGvrpStatisticsSJE,'rlPortGvrpStatisticsSJIn':rlPortGvrpStatisticsSJIn,'rlPortGvrpStatisticsSEmp':rlPortGvrpStatisticsSEmp,'rlPortGvrpStatisticsSLIn':rlPortGvrpStatisticsSLIn,'rlPortGvrpStatisticsSLE':rlPortGvrpStatisticsSLE,'rlPortGvrpStatisticsSLA':rlPortGvrpStatisticsSLA,'rlPortGvrpStatisticsClear':rlPortGvrpStatisticsClear,'rlPortGvrpErrorStatisticsTable':rlPortGvrpErrorStatisticsTable,'rlPortGvrpErrorStatisticsEntry':rlPortGvrpErrorStatisticsEntry,'rlPortGvrpErrorStatisticsInvProt':rlPortGvrpErrorStatisticsInvProt,'rlPortGvrpErrorStatisticsInvAtyp':rlPortGvrpErrorStatisticsInvAtyp,'rlPortGvrpErrorStatisticsInvAval':rlPortGvrpErrorStatisticsInvAval,'rlPortGvrpErrorStatisticsInvPlen':rlPortGvrpErrorStatisticsInvPlen,'rlPortGvrpErrorStatisticsInvAlen':rlPortGvrpErrorStatisticsInvAlen,'rlPortGvrpErrorStatisticsInvEvent':rlPortGvrpErrorStatisticsInvEvent,'rlPortGvrpErrorStatisticsClear':rlPortGvrpErrorStatisticsClear,'rlPortGvrpApplicantStatusTable':rlPortGvrpApplicantStatusTable,'rlPortGvrpApplicantStatusEntry':rlPortGvrpApplicantStatusEntry,'rlPortGvrpApplicantStatusValue':rlPortGvrpApplicantStatusValue,'rlPortGvrpRegistrationModeTable':rlPortGvrpRegistrationModeTable,'rlPortGvrpRegistrationModeEntry':rlPortGvrpRegistrationModeEntry,'rlPortGvrpRegistrationModeForbidden':rlPortGvrpRegistrationModeForbidden})