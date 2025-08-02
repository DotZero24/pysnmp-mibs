_H='trapOID-ces'
_G='trapSysUpTime-ces'
_F='trapDescription-ces'
_E='trapSeverity-ces'
_D='not-accessible'
_C='read-only'
_B='CONTIVITY-TRAP-ACKNOWLEDGMENT-MIB'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
snmpAgentInfo_Utilities_ces,=mibBuilder.importSymbols('CONTIVITY-INFO-V1-MIB','snmpAgentInfo-Utilities-ces')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
snmpAgentInfo_Utilities_TrapAck_ces=ModuleIdentity((1,3,6,1,4,1,2505,1,15,1,2))
_TrapAck_RevInfo_ces_ObjectIdentity=ObjectIdentity
trapAck_RevInfo_ces=_TrapAck_RevInfo_ces_ObjectIdentity((1,3,6,1,4,1,2505,1,15,1,2,1))
_TrapAck_RevDate_ces_Type=DisplayString
_TrapAck_RevDate_ces_Object=MibScalar
trapAck_RevDate_ces=_TrapAck_RevDate_ces_Object((1,3,6,1,4,1,2505,1,15,1,2,1,1),_TrapAck_RevDate_ces_Type())
trapAck_RevDate_ces.setMaxAccess(_C)
if mibBuilder.loadTexts:trapAck_RevDate_ces.setStatus(_A)
_TrapAck_Rev_ces_Type=Integer32
_TrapAck_Rev_ces_Object=MibScalar
trapAck_Rev_ces=_TrapAck_Rev_ces_Object((1,3,6,1,4,1,2505,1,15,1,2,1,2),_TrapAck_Rev_ces_Type())
trapAck_Rev_ces.setMaxAccess(_C)
if mibBuilder.loadTexts:trapAck_Rev_ces.setStatus(_A)
_TrapAck_ServerRev_ces_Type=DisplayString
_TrapAck_ServerRev_ces_Object=MibScalar
trapAck_ServerRev_ces=_TrapAck_ServerRev_ces_Object((1,3,6,1,4,1,2505,1,15,1,2,1,3),_TrapAck_ServerRev_ces_Type())
trapAck_ServerRev_ces.setMaxAccess(_C)
if mibBuilder.loadTexts:trapAck_ServerRev_ces.setStatus(_A)
_TrapSeverity_ces_Type=Integer32
_TrapSeverity_ces_Object=MibScalar
trapSeverity_ces=_TrapSeverity_ces_Object((1,3,6,1,4,1,2505,1,15,1,2,2),_TrapSeverity_ces_Type())
trapSeverity_ces.setMaxAccess(_D)
if mibBuilder.loadTexts:trapSeverity_ces.setStatus(_A)
_TrapDescription_ces_Type=Integer32
_TrapDescription_ces_Object=MibScalar
trapDescription_ces=_TrapDescription_ces_Object((1,3,6,1,4,1,2505,1,15,1,2,3),_TrapDescription_ces_Type())
trapDescription_ces.setMaxAccess(_D)
if mibBuilder.loadTexts:trapDescription_ces.setStatus(_A)
_TrapSysUpTime_ces_Type=Integer32
_TrapSysUpTime_ces_Object=MibScalar
trapSysUpTime_ces=_TrapSysUpTime_ces_Object((1,3,6,1,4,1,2505,1,15,1,2,4),_TrapSysUpTime_ces_Type())
trapSysUpTime_ces.setMaxAccess(_D)
if mibBuilder.loadTexts:trapSysUpTime_ces.setStatus(_A)
_TrapOID_ces_Type=ObjectIdentifier
_TrapOID_ces_Object=MibScalar
trapOID_ces=_TrapOID_ces_Object((1,3,6,1,4,1,2505,1,15,1,2,5),_TrapOID_ces_Type())
trapOID_ces.setMaxAccess(_D)
if mibBuilder.loadTexts:trapOID_ces.setStatus(_A)
_TrapAckTable_ces_Object=MibTable
trapAckTable_ces=_TrapAckTable_ces_Object((1,3,6,1,4,1,2505,1,15,1,2,6))
if mibBuilder.loadTexts:trapAckTable_ces.setStatus(_A)
_TrapAckEntry_ces_Object=MibTableRow
trapAckEntry_ces=_TrapAckEntry_ces_Object((1,3,6,1,4,1,2505,1,15,1,2,6,1))
trapAckEntry_ces.setIndexNames((0,_B,_E),(0,_B,_F),(0,_B,_G),(0,_B,_H))
if mibBuilder.loadTexts:trapAckEntry_ces.setStatus(_A)
_TrapAcknowledgement_ces_Type=Integer32
_TrapAcknowledgement_ces_Object=MibTableColumn
trapAcknowledgement_ces=_TrapAcknowledgement_ces_Object((1,3,6,1,4,1,2505,1,15,1,2,6,1,1),_TrapAcknowledgement_ces_Type())
trapAcknowledgement_ces.setMaxAccess(_C)
if mibBuilder.loadTexts:trapAcknowledgement_ces.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'snmpAgentInfo-Utilities-TrapAck-ces':snmpAgentInfo_Utilities_TrapAck_ces,'trapAck-RevInfo-ces':trapAck_RevInfo_ces,'trapAck-RevDate-ces':trapAck_RevDate_ces,'trapAck-Rev-ces':trapAck_Rev_ces,'trapAck-ServerRev-ces':trapAck_ServerRev_ces,_E:trapSeverity_ces,_F:trapDescription_ces,_G:trapSysUpTime_ces,_H:trapOID_ces,'trapAckTable-ces':trapAckTable_ces,'trapAckEntry-ces':trapAckEntry_ces,'trapAcknowledgement-ces':trapAcknowledgement_ces})