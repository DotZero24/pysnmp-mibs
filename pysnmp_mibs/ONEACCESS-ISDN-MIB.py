_I='current'
_H='ifType'
_G='ifOperStatus'
_F='ifName'
_E='ifIndex'
_D='ifDescr'
_C='ifAlias'
_B='ifAdminStatus'
_A='IF-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifAdminStatus,ifAlias,ifDescr,ifIndex,ifName,ifOperStatus,ifType=mibBuilder.importSymbols(_A,_B,_C,_D,_E,_F,_G,_H)
oacEventText,=mibBuilder.importSymbols('ONEACCESS-EVENTS-MIB','oacEventText')
oacExpIMIsdn,oacExpIMIsdnNotifications,oacMIBModules=mibBuilder.importSymbols('ONEACCESS-GLOBAL-REG','oacExpIMIsdn','oacExpIMIsdnNotifications','oacMIBModules')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
oacIsdnMIBModule=ModuleIdentity((1,3,6,1,4,1,13191,1,100,674))
if mibBuilder.loadTexts:oacIsdnMIBModule.setRevisions(('2011-10-27 00:00',))
dialDown=NotificationType((1,3,6,1,4,1,13191,10,3,7,0,3))
dialDown.setObjects(*((_A,_E),(_A,_D),(_A,_H),(_A,_B),(_A,_G),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:dialDown.setStatus(_I)
dialUp=NotificationType((1,3,6,1,4,1,13191,10,3,7,0,4))
dialUp.setObjects(*((_A,_E),(_A,_D),(_A,_H),(_A,_B),(_A,_G),(_A,_F),(_A,_C)))
if mibBuilder.loadTexts:dialUp.setStatus(_I)
mibBuilder.exportSymbols('ONEACCESS-ISDN-MIB',**{'oacIsdnMIBModule':oacIsdnMIBModule,'dialDown':dialDown,'dialUp':dialUp})