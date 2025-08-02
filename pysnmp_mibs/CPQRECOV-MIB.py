_E='NotificationType'
_D='sysName'
_C='SNMPv2-MIB'
_B='cpqHoTrapFlags'
_A='CPQHOST-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
compaq,cpqHoTrapFlags=mibBuilder.importSymbols(_A,'compaq',_B)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
sysName,=mibBuilder.importSymbols(_C,_D)
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier',_E,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_E,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_CpqRecovery_ObjectIdentity=ObjectIdentity
cpqRecovery=_CpqRecovery_ObjectIdentity((1,3,6,1,4,1,232,13))
cpqRsPartnerFailed=NotificationType((1,3,6,1,4,1,232,0,13001))
cpqRsPartnerFailed.setObjects(*((_C,_D),(_A,_B)))
if mibBuilder.loadTexts:cpqRsPartnerFailed.setStatus('')
cpqRsStandbyCableFailure=NotificationType((1,3,6,1,4,1,232,0,13002))
cpqRsStandbyCableFailure.setObjects(*((_C,_D),(_A,_B)))
if mibBuilder.loadTexts:cpqRsStandbyCableFailure.setStatus('')
cpqRsStandbyFailure=NotificationType((1,3,6,1,4,1,232,0,13003))
cpqRsStandbyFailure.setObjects(*((_C,_D),(_A,_B)))
if mibBuilder.loadTexts:cpqRsStandbyFailure.setStatus('')
cpqRsOnlineCableFailure=NotificationType((1,3,6,1,4,1,232,0,13004))
cpqRsOnlineCableFailure.setObjects(*((_C,_D),(_A,_B)))
if mibBuilder.loadTexts:cpqRsOnlineCableFailure.setStatus('')
cpqRsFailoverFailed=NotificationType((1,3,6,1,4,1,232,0,13005))
cpqRsFailoverFailed.setObjects(*((_C,_D),(_A,_B)))
if mibBuilder.loadTexts:cpqRsFailoverFailed.setStatus('')
mibBuilder.exportSymbols('CPQRECOV-MIB',**{'cpqRsPartnerFailed':cpqRsPartnerFailed,'cpqRsStandbyCableFailure':cpqRsStandbyCableFailure,'cpqRsStandbyFailure':cpqRsStandbyFailure,'cpqRsOnlineCableFailure':cpqRsOnlineCableFailure,'cpqRsFailoverFailed':cpqRsFailoverFailed,'cpqRecovery':cpqRecovery})