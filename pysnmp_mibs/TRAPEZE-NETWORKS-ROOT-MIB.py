if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
trpzRootMib=ModuleIdentity((1,3,6,1,4,1,14525))
if mibBuilder.loadTexts:trpzRootMib.setRevisions(('2008-05-22 00:08','2007-11-28 00:07','2006-04-14 00:06','2005-01-01 00:00'))
_TrpzProducts_ObjectIdentity=ObjectIdentity
trpzProducts=_TrpzProducts_ObjectIdentity((1,3,6,1,4,1,14525,1))
_TrpzTemporary_ObjectIdentity=ObjectIdentity
trpzTemporary=_TrpzTemporary_ObjectIdentity((1,3,6,1,4,1,14525,2))
_TrpzRegistration_ObjectIdentity=ObjectIdentity
trpzRegistration=_TrpzRegistration_ObjectIdentity((1,3,6,1,4,1,14525,3))
_TrpzMibs_ObjectIdentity=ObjectIdentity
trpzMibs=_TrpzMibs_ObjectIdentity((1,3,6,1,4,1,14525,4))
_TrpzTraps_ObjectIdentity=ObjectIdentity
trpzTraps=_TrpzTraps_ObjectIdentity((1,3,6,1,4,1,14525,5))
_TrpzMgmtAppMibs_ObjectIdentity=ObjectIdentity
trpzMgmtAppMibs=_TrpzMgmtAppMibs_ObjectIdentity((1,3,6,1,4,1,14525,6))
mibBuilder.exportSymbols('TRAPEZE-NETWORKS-ROOT-MIB',**{'trpzRootMib':trpzRootMib,'trpzProducts':trpzProducts,'trpzTemporary':trpzTemporary,'trpzRegistration':trpzRegistration,'trpzMibs':trpzMibs,'trpzTraps':trpzTraps,'trpzMgmtAppMibs':trpzMgmtAppMibs})