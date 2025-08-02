_C='mandatory'
_B='read-write'
_A='DisplayString'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_A,'PhysAddress','TextualConvention')
_A3Com_ObjectIdentity=ObjectIdentity
a3Com=_A3Com_ObjectIdentity((1,3,6,1,4,1,43))
_SwitchingSystemsMibs_ObjectIdentity=ObjectIdentity
switchingSystemsMibs=_SwitchingSystemsMibs_ObjectIdentity((1,3,6,1,4,1,43,29))
_A3ComSwitchingSystemsMib_ObjectIdentity=ObjectIdentity
a3ComSwitchingSystemsMib=_A3ComSwitchingSystemsMib_ObjectIdentity((1,3,6,1,4,1,43,29,4))
_A3ComWebConfig_ObjectIdentity=ObjectIdentity
a3ComWebConfig=_A3ComWebConfig_ObjectIdentity((1,3,6,1,4,1,43,29,4,24))
class _A3ComWebConfigHelpServer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,85))
_A3ComWebConfigHelpServer_Type.__name__=_A
_A3ComWebConfigHelpServer_Object=MibScalar
a3ComWebConfigHelpServer=_A3ComWebConfigHelpServer_Object((1,3,6,1,4,1,43,29,4,24,1),_A3ComWebConfigHelpServer_Type())
a3ComWebConfigHelpServer.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComWebConfigHelpServer.setStatus(_C)
class _A3ComWebConfigEmailServerAddress_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,85))
_A3ComWebConfigEmailServerAddress_Type.__name__=_A
_A3ComWebConfigEmailServerAddress_Object=MibScalar
a3ComWebConfigEmailServerAddress=_A3ComWebConfigEmailServerAddress_Object((1,3,6,1,4,1,43,29,4,24,2),_A3ComWebConfigEmailServerAddress_Type())
a3ComWebConfigEmailServerAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComWebConfigEmailServerAddress.setStatus(_C)
class _A3ComWebConfigEmailAddresses_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_A3ComWebConfigEmailAddresses_Type.__name__=_A
_A3ComWebConfigEmailAddresses_Object=MibScalar
a3ComWebConfigEmailAddresses=_A3ComWebConfigEmailAddresses_Object((1,3,6,1,4,1,43,29,4,24,3),_A3ComWebConfigEmailAddresses_Type())
a3ComWebConfigEmailAddresses.setMaxAccess(_B)
if mibBuilder.loadTexts:a3ComWebConfigEmailAddresses.setStatus(_C)
mibBuilder.exportSymbols('A3COM-SWITCHING-SYSTEMS-WEBSERVER-MIB',**{'a3Com':a3Com,'switchingSystemsMibs':switchingSystemsMibs,'a3ComSwitchingSystemsMib':a3ComSwitchingSystemsMib,'a3ComWebConfig':a3ComWebConfig,'a3ComWebConfigHelpServer':a3ComWebConfigHelpServer,'a3ComWebConfigEmailServerAddress':a3ComWebConfigEmailServerAddress,'a3ComWebConfigEmailAddresses':a3ComWebConfigEmailAddresses})