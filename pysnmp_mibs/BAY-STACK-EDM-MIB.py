_D='current'
_C='read-write'
_B='Integer32'
_A='OctetString'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_A,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bayStackMibs,=mibBuilder.importSymbols('SYNOPTICS-ROOT-MIB','bayStackMibs')
bayStackEdmMib=ModuleIdentity((1,3,6,1,4,1,45,5,36))
if mibBuilder.loadTexts:bayStackEdmMib.setRevisions(('2013-10-11 00:00','2013-02-13 00:00','2009-08-20 00:00'))
_BayStackEdmNotifications_ObjectIdentity=ObjectIdentity
bayStackEdmNotifications=_BayStackEdmNotifications_ObjectIdentity((1,3,6,1,4,1,45,5,36,0))
_BayStackEdmObjects_ObjectIdentity=ObjectIdentity
bayStackEdmObjects=_BayStackEdmObjects_ObjectIdentity((1,3,6,1,4,1,45,5,36,1))
_BsEdmScalars_ObjectIdentity=ObjectIdentity
bsEdmScalars=_BsEdmScalars_ObjectIdentity((1,3,6,1,4,1,45,5,36,1,1))
class _BsEdmHelpFilePath_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,327))
_BsEdmHelpFilePath_Type.__name__=_A
_BsEdmHelpFilePath_Object=MibScalar
bsEdmHelpFilePath=_BsEdmHelpFilePath_Object((1,3,6,1,4,1,45,5,36,1,1,1),_BsEdmHelpFilePath_Type())
bsEdmHelpFilePath.setMaxAccess(_C)
if mibBuilder.loadTexts:bsEdmHelpFilePath.setStatus(_D)
class _BsEdmInactivityTimeout_Type(Integer32):defaultValue=900;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(30,65535))
_BsEdmInactivityTimeout_Type.__name__=_B
_BsEdmInactivityTimeout_Object=MibScalar
bsEdmInactivityTimeout=_BsEdmInactivityTimeout_Object((1,3,6,1,4,1,45,5,36,1,1,2),_BsEdmInactivityTimeout_Type())
bsEdmInactivityTimeout.setMaxAccess(_C)
if mibBuilder.loadTexts:bsEdmInactivityTimeout.setStatus(_D)
if mibBuilder.loadTexts:bsEdmInactivityTimeout.setUnits('seconds')
mibBuilder.exportSymbols('BAY-STACK-EDM-MIB',**{'bayStackEdmMib':bayStackEdmMib,'bayStackEdmNotifications':bayStackEdmNotifications,'bayStackEdmObjects':bayStackEdmObjects,'bsEdmScalars':bsEdmScalars,'bsEdmHelpFilePath':bsEdmHelpFilePath,'bsEdmInactivityTimeout':bsEdmInactivityTimeout})